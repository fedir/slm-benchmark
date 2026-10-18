#!/usr/bin/env python3
"""Benchmark local GGUF models through llama-server.

  run.py                      run every model in models.json on every question
  run.py -m mimo-9b,deepseek-r1-8b -q regex-ipv4
  run.py --force              redo results that already exist
  run.py --summary            only rebuild results/SUMMARY.md

Each (model, question) is saved as results/<model>/<question-id>.md (+ .json metadata).
"""
import argparse, glob, json, os, re, subprocess, sys, tempfile, time, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "results")
PORT = int(os.environ.get("BENCH_PORT", "8089"))   # BENCH_PORT lets a side test run next to a benchmark
BACKEND = glob.glob("/var/lib/flatpak/app/ai.lmstudio.lm-studio/x86_64/stable/active/files/extra/"
                    "lmstudio/resources/app/.webpack/bin/extensions/backends/llama.cpp-linux-x86_64-vulkan-avx2-*")[0]
PARAMS = {"max_tokens": 512, "temperature": 0.6, "top_p": 0.95, "top_k": 20, "seed": 42,
          "chat_template_kwargs": {"enable_thinking": False}}

def post(body):
    r = urllib.request.Request(f"http://localhost:{PORT}/v1/chat/completions", json.dumps(body).encode(),
                               {"Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(r, timeout=1800))

def code_blocks(text):
    return [b.strip("\n") for b in re.findall(r"```[a-zA-Z0-9_+-]*\n(.*?)```", text, re.S)]

def norm_rows(rows):
    return [tuple(round(v, 6) if isinstance(v, float) else v for v in r) for r in rows]

def sql_rows(setup, query):
    """Run one read-only query on an in-memory SQLite database built from `setup`; returns the rows (raises on error or after 5 s)."""
    import sqlite3
    con = sqlite3.connect(":memory:"); con.executescript(setup)
    ok = {sqlite3.SQLITE_SELECT, sqlite3.SQLITE_READ, sqlite3.SQLITE_FUNCTION, sqlite3.SQLITE_RECURSIVE}
    con.set_authorizer(lambda action, *a: sqlite3.SQLITE_OK if action in ok else sqlite3.SQLITE_DENY)
    t0 = time.time(); con.set_progress_handler(lambda: 1 if time.time() - t0 > 5 else 0, 100000)
    return norm_rows(con.execute(query).fetchall())

def sql_check(setup, expected, ordered, answer):
    blocks = code_blocks(answer)
    query = (blocks[0] if blocks else answer).strip()
    try:
        got = sql_rows(setup, query)
    except Exception as e:
        return False, f"the query fails: {type(e).__name__}: {e}"
    want = norm_rows(expected)
    if not ordered: got, want_c = sorted(got, key=repr), sorted(want, key=repr)
    else: want_c = want
    if got == want_c: return True, "rows match"
    return False, f"returned {got[:6]!r}{' ...' if len(got) > 6 else ''} ({len(got)} rows), expected {want[:6]!r}{' ...' if len(want) > 6 else ''} ({len(want)} rows)"

def sh_run(files, cmd, post=None, timeout=10):
    """Run a bash command in a bubblewrap sandbox (read-only system, private /tmp and /home, no network) on fixture files in the
    working directory; returns stdout of `cmd`, or of `post` if given (post lists the final state)."""
    with tempfile.TemporaryDirectory() as d:
        for n, t in files.items(): open(os.path.join(d, n), "w").write(t)
        def sandbox(script):
            return subprocess.run(["bwrap", "--unshare-all", "--ro-bind", "/", "/", "--tmpfs", "/home", "--tmpfs", "/tmp", "--dev", "/dev",
                                   "--proc", "/proc", "--bind", d, "/tmp/work", "--chdir", "/tmp/work", "bash", "-c", script],
                                  capture_output=True, text=True, timeout=timeout, stdin=subprocess.DEVNULL,
                                  env={"PATH": "/usr/bin:/bin", "LC_ALL": "C", "HOME": "/tmp"})
        p = sandbox(cmd)
        if post: p = sandbox(post)
        return p.stdout

def norm_lines(text):
    return [" ".join(l.split()) for l in text.strip().splitlines()]

def sh_check(files, expected, post, answer):
    blocks = code_blocks(answer)
    cmd = re.sub(r"^\$ ", "", (blocks[0] if blocks else answer).strip(), flags=re.M)
    try:
        got = norm_lines(sh_run(files, cmd, post))
    except subprocess.TimeoutExpired:
        return False, "the command did not finish in 10 s"
    want = norm_lines(expected)
    if got == want: return True, "output matches"
    return False, f"output {got[:6]!r}, expected {want[:6]!r}"

def check(q, answer):
    """Return (passed, detail)."""
    blocks = code_blocks(answer)
    unfenced = False
    if q["type"] == "regex":
        pat = (blocks[0] if blocks else answer).strip()
        mq = re.match(r"^r?(['\"])(.*)\1$", pat, re.S)      # strip a python string wrapper like r'...'
        pat = mq.group(2) if mq else pat
        pat = pat.strip("/") if pat.startswith("/") and pat.count("/") >= 2 else pat
        try:
            rx = re.compile(pat)
        except re.error as e:
            return False, f"invalid regex {pat!r}: {e}"
        bad = [s for s in q["match"] if not rx.fullmatch(s)] + [f"!{s}" for s in q["nomatch"] if rx.fullmatch(s)]
        return not bad, f"regex {pat!r}" + (f"; wrong on {bad}" if bad else "")
    if q["type"] == "python":
        code = next((b for b in blocks if f"def {q['func']}" in b), None)
        if code is None and not blocks and f"def {q['func']}" in answer:
            code = answer          # correct code but not fenced as requested; graded on the algorithm
            unfenced = True
        if code is None:
            return False, "no code block defining " + q["func"]
        with tempfile.TemporaryDirectory() as d:
            f = os.path.join(d, "t.py")
            open(f, "w").write(code + "\n\n" + q["test"])
            try:
                p = subprocess.run([sys.executable, "-I", f], cwd=d, capture_output=True, text=True, timeout=30)
            except subprocess.TimeoutExpired:
                return False, "timeout"
            tail = (p.stderr.strip().splitlines() or [""])[-1]
            return p.returncode == 0, ("tests passed" if p.returncode == 0 else tail) + (" (no code fence)" if unfenced else "")
    if q["type"] == "sql":
        return sql_check(q["setup"], q["expected"], q.get("ordered", False), answer)
    if q["type"] == "shell":
        return sh_check(q["files"], q["expected"], q.get("post"), answer)
    if q["type"] == "tokens":
        cmd = (blocks[0] if blocks else answer).replace("'", "").replace('"', "")   # quoting a flag value changes nothing
        miss = [alts[0] for alts in q["tokens"] if not any(re.search(a, cmd) for a in alts)]
        return not miss, "all parts present" if not miss else f"missing {miss}"

def run_model(name, spec, questions, force):
    todo = [q for q in questions if force or not os.path.exists(f"{RES}/{name}/{q['id']}.json")]
    if not todo:
        print(f"[{name}] nothing to do"); return
    os.makedirs(f"{RES}/{name}", exist_ok=True)
    env = dict(os.environ, LD_LIBRARY_PATH=BACKEND)
    cmd = [f"{BACKEND}/llama-server", "-m", os.path.expanduser(spec["path"]), "-ngl", "0", "-t", "4",
           "-c", "4096", "--port", str(PORT), "--no-webui"] + spec["args"]
    srv = subprocess.Popen(cmd, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        for _ in range(180):
            try: urllib.request.urlopen(f"http://localhost:{PORT}/health", timeout=2); break
            except Exception:
                if srv.poll() is not None: raise SystemExit(f"[{name}] server died on startup")
                time.sleep(2)
        for q in todo:
            t0 = time.time()
            d = post({"messages": [{"role": "user", "content": q["prompt"]}], **PARAMS})
            dt = time.time() - t0
            m = d["choices"][0]["message"]
            ans, reasoning = m.get("content") or "", m.get("reasoning_content") or ""
            ok, detail = check(q, ans)
            n = d["usage"]["completion_tokens"]
            meta = {"model": name, "question": q["id"], "category": q["category"], "passed": ok, "detail": detail,
                    "completion_tokens": n, "seconds": round(dt, 1), "tps": round(n / dt, 2),
                    "finish_reason": d["choices"][0]["finish_reason"], "reasoning_chars": len(reasoning)}
            json.dump(meta, open(f"{RES}/{name}/{q['id']}.json", "w"), indent=1)
            with open(f"{RES}/{name}/{q['id']}.md", "w") as f:
                f.write(f"# {name} / {q['id']}\n\n- category: {q['category']}\n- result: **{'PASS' if ok else 'FAIL'}** ({detail})\n"
                        f"- tokens: {n} in {dt:.0f}s ({n/dt:.1f} t/s), finish: {meta['finish_reason']}\n\n"
                        f"## Prompt\n\n{q['prompt']}\n\n## Answer\n\n{ans}\n")
                if reasoning:
                    f.write(f"\n## Reasoning\n\n{reasoning}\n")
            print(f"[{name}] {q['id']:22} {'PASS' if ok else 'FAIL'}  {n:4d} tok  {n/dt:4.1f} t/s  {detail[:70]}", flush=True)
    finally:
        srv.terminate(); srv.wait()

def regrade(models, questions):
    """Re-run the checkers on saved answers (no model needed)."""
    for name in models:
        for q in questions:
            mp, jp = f"{RES}/{name}/{q['id']}.md", f"{RES}/{name}/{q['id']}.json"
            if not os.path.exists(jp): continue
            txt = open(mp).read()
            ans = txt.split("## Answer\n\n", 1)[1].split("\n## Reasoning\n", 1)[0]
            ok, detail = check(q, ans)
            meta = json.load(open(jp)); meta.update(passed=ok, detail=detail)
            json.dump(meta, open(jp, "w"), indent=1)
            txt = re.sub(r"- result: \*\*(PASS|FAIL)\*\* \(.*\)", lambda m: f"- result: **{'PASS' if ok else 'FAIL'}** ({detail})", txt, count=1)
            open(mp, "w").write(txt)

def summary(models, questions):
    rows, cats = [], sorted({q["category"] for q in questions})
    out = ["# Benchmark summary\n", f"Sampling: temp {PARAMS['temperature']}, top_p {PARAMS['top_p']}, top_k {PARAMS['top_k']}, "
           f"seed {PARAMS['seed']}, max_tokens {PARAMS['max_tokens']}, thinking requested off. CPU, 4 threads.\n"]
    head = "| model | " + " | ".join(cats) + " | total | avg t/s | avg s/answer | truncated |\n|---|" + "---|" * (len(cats) + 4)
    out.append(head)
    for name in models:
        ms = [json.load(open(p)) for p in sorted(glob.glob(f"{RES}/{name}/*.json"))]
        if not ms: continue
        cell = lambda c: "%d/%d" % (sum(m["passed"] for m in ms if m["category"] == c), sum(m["category"] == c for m in ms))
        out.append(f"| {name} | " + " | ".join(cell(c) for c in cats) +
                   f" | {sum(m['passed'] for m in ms)}/{len(ms)} | {sum(m['tps'] for m in ms)/len(ms):.1f} | "
                   f"{sum(m['seconds'] for m in ms)/len(ms):.0f} | {sum(m['finish_reason'] == 'length' for m in ms)} |")
    out.append("\n## Per question\n\n| question | " + " | ".join(models) + " |\n|---|" + "---|" * len(models))
    for q in questions:
        cells = []
        for name in models:
            p = f"{RES}/{name}/{q['id']}.json"
            cells.append(("PASS" if json.load(open(p))["passed"] else "FAIL") if os.path.exists(p) else "-")
        out.append(f"| {q['id']} | " + " | ".join(cells) + " |")
    open(f"{RES}/SUMMARY.md", "w").write("\n".join(out) + "\n")
    print("\n".join(out))

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-m", "--models"); ap.add_argument("-q", "--questions")
    ap.add_argument("--force", action="store_true"); ap.add_argument("--summary", action="store_true"); ap.add_argument("--regrade", action="store_true")
    a = ap.parse_args()
    models = json.load(open(f"{HERE}/models.json"))
    questions = json.load(open(f"{HERE}/questions.json"))
    if a.questions: questions = [q for q in questions if q["id"] in a.questions.split(",")]
    sel = a.models.split(",") if a.models else list(models)
    if a.regrade: regrade(sel, questions)
    if not (a.summary or a.regrade):
        for n in sel: run_model(n, models[n], questions, a.force)
    summary(sel, questions)
