#!/usr/bin/env python3
"""Repeated benchmark runs (stability) and the generate -> verify -> retry harness.

  repeat.py --mode naked   -m ornith-9b-mtp            3 seeds, one attempt per question
  repeat.py --mode harness -m mimo-9b,qwen2.5-coder-3b 3 seeds, verifier + up to 2 retries
  repeat.py --stats                                    rebuild runs/STATS.md from saved runs
  repeat.py --regrade                                  re-grade saved answers (after a grader fix), then rebuild stats

Results: runs/<mode>/<model>/seed<N>/<question>.json (+ .md transcript). Existing files are
skipped, so an interrupted batch can be resumed. Hidden grading is always run.check() from run.py.
The harness first attempt is the same request as a naked run (same seed and params), so a
harness run also contains the naked result for that seed (attempts[0]).
"""
import argparse, glob, json, os, re, shlex, shutil, statistics as st, subprocess, sys, tempfile, time, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import run as base

RUNS = os.path.join(HERE, "runs")
SAMPLE = {}                  # sampling overrides for this invocation (profile and/or command-line values)
PROFILE = "default"
KUBECTL_SEMANTIC = True      # False reproduces the original syntax-only kubectl verifier
PUBLIC = json.load(open(f"{HERE}/public.json"))
CONN = re.compile(r"Unable to connect|dial tcp|connection refused|network is unreachable|[Cc]ouldn't get|"
                  r"no route to host|i/o timeout|context deadline|memcache", re.I)
ASK = {"regex": "regex", "python": "code in one code block", "tokens": "command", "sql": "SQL query", "shell": "bash command"}

PY_RUNNER = r'''
import json, sys, time
spec = json.load(open(sys.argv[1])); src = open(sys.argv[2]).read(); ns = {}
try:
    exec(compile(src, "answer.py", "exec"), ns)
except Exception as e:
    print(json.dumps({"error": f"the code does not run: {type(e).__name__}: {e}"})); sys.exit(0)
if spec["func"] not in ns:
    print(json.dumps({"error": f"no function {spec['func']} is defined"})); sys.exit(0)
fails = []
for call, expected in spec["cases"]:
    try:
        got = eval(call, ns)
    except Exception as e:
        fails.append(f"{call} raised {type(e).__name__}: {e}"); continue
    if got != eval(expected, ns):
        fails.append(f"{call} returned {got!r}, expected {expected}")
if spec.get("perf"):
    try:
        t = time.time(); exec(spec["perf"], ns); dt = time.time() - t
        if dt > spec["perf_limit"]:
            fails.append(f"too slow: {dt:.1f}s on {spec['perf_label']} (limit {spec['perf_limit']}s)")
    except Exception as e:
        fails.append(f"the performance example raised {type(e).__name__}: {e}")
print(json.dumps({"fails": fails}))
'''

# ---------------------------------------------------------------- verifier (public examples only)
def verify_regex(q, pub, answer):
    ok, detail = base.check({**q, "match": pub["match"], "nomatch": pub["nomatch"]}, answer)
    if ok: return True, ""
    m = re.search(r"wrong on (\[.*\])", detail)
    if not m: return False, detail
    import ast
    bad = ast.literal_eval(m.group(1))
    should_not = [s[1:] for s in bad if s.startswith("!")]
    should = [s for s in bad if not s.startswith("!")]
    parts = []
    if should: parts.append(f"it does not match these, which it should: {should}")
    if should_not: parts.append(f"it matches these, which it must reject: {should_not}")
    return False, "; ".join(parts)

def verify_python(q, pub, answer):
    blocks = base.code_blocks(answer)
    code = next((b for b in blocks if f"def {q['func']}" in b), None)
    if code is None and not blocks and f"def {q['func']}" in answer: code = answer
    if code is None: return False, f"no code block defining {q['func']}"
    with tempfile.TemporaryDirectory() as d:
        for name, text in (("spec.json", json.dumps(pub)), ("answer.py", code), ("runner.py", PY_RUNNER)):
            open(f"{d}/{name}", "w").write(text)
        try:
            p = subprocess.run([sys.executable, "-I", f"{d}/runner.py", f"{d}/spec.json", f"{d}/answer.py"],
                               cwd=d, capture_output=True, text=True, timeout=20)
        except subprocess.TimeoutExpired:
            return False, f"too slow: timed out after 20 s on {pub.get('perf_label', 'the examples')}"
        try:
            out = json.loads(p.stdout.strip().splitlines()[-1])
        except Exception:
            return False, (p.stderr.strip().splitlines() or ["the code crashed"])[-1]
    if "error" in out: return False, out["error"]
    return (not out["fails"]), "; ".join(out["fails"])

# kubectl flags that take a value (pflag syntax: -n prod, -nprod, -n=prod, --namespace prod, --namespace=prod)
KUBE_SHORT = {"n": "namespace", "c": "container", "o": "output", "l": "selector", "L": "label-columns"}
KUBE_LONG = {"namespace", "container", "output", "selector", "sort-by", "tail", "replicas", "context", "cluster", "user",
             "kubeconfig", "field-selector", "since", "since-time", "limit-bytes", "request-timeout", "template",
             "label-columns", "server", "token", "filename", "for", "timeout"}
KUBE_KIND = {"po": "pods", "pod": "pods", "pods": "pods", "deploy": "deployment", "deployment": "deployment",
             "deployments": "deployment", "no": "nodes", "node": "nodes", "nodes": "nodes",
             "ev": "events", "event": "events", "events": "events"}

def kube_parse(argv):
    """Structured view of a kubectl command: {'verb', 'args' (positionals after the verb), 'flags' {long name: value|True}}."""
    flags, pos, dd, i, rest = {}, [], [], 0, argv[1:]
    short = dict(KUBE_SHORT)
    if "logs" in rest: short["f"] = None            # `-f` is --follow for logs, --filename elsewhere
    else: short["f"] = "filename"
    while i < len(rest):
        t = rest[i]; i += 1
        if t == "--": dd = rest[i:]; break
        if t.startswith("--"):
            name, eq, val = t[2:].partition("=")
            if name in KUBE_LONG and not eq:
                val = rest[i] if i < len(rest) else ""; i += 1
            flags[name] = val if (eq or name in KUBE_LONG) else True
            if eq and val in ("false", "False") and name not in KUBE_LONG: flags[name] = False
        elif t.startswith("-") and len(t) > 1:
            for j, ch in enumerate(t[1:], 1):
                if ch in short and short[ch]:
                    val = t[j + 1:].lstrip("=")
                    if not val: val = rest[i] if i < len(rest) else ""; i += 1
                    flags[short[ch]] = val; break
                flags[{"f": "follow", "A": "all-namespaces", "w": "watch"}.get(ch, ch)] = True
        else:
            pos.append(t)
    return {"verb": pos[0] if pos else "", "args": pos[1:], "flags": flags, "dashdash": dd}

def kube_target(args):
    """(kind, name, rest) from 'TYPE NAME', 'TYPE/NAME' or 'NAME' positionals."""
    if args and "/" in args[0]:
        kind, name = args[0].split("/", 1); return kind, name, args[1:]
    return (args[0] if args else ""), (args[1] if len(args) > 1 else ""), args[2:]

def kube_intent_problems(argv, intent):
    """Compare the command with the task requirements (public.json 'intent'); returns a list of plain-language problems."""
    c, fl, probs = kube_parse(argv), None, []
    fl = c["flags"]
    if c["verb"] != intent["verb"]:
        return [f"the kubectl subcommand should be `{intent['verb']}`, not `{c['verb'] or 'none'}`"]
    args = c["args"]
    if intent["verb"] == "logs":
        name, extra = (args[0].split("/", 1)[-1] if args else ""), args[1:]
        kind = args[0].split("/", 1)[0] if args and "/" in args[0] else "pod"
        if kind not in ("pod", "pods", "po") or name != intent["name"]:
            probs.append(f"the target should be pod `{intent['name']}`")
        container = fl.get("container") or (extra[0] if extra else None)
        if container != intent["container"]:
            probs.append(f"the container to read should be `{intent['container']}`, the command selects {container!r}")
    elif intent["verb"] == "exec":
        pod = args[0].split("/", 1)[-1] if args else ""
        if pod != intent["name"]: probs.append(f"the target should be pod `{intent['name']}`")
        if c["dashdash"] != intent["dashdash"]:
            probs.append(f"the command to run should come after `--` and be `{' '.join(intent['dashdash'])}`, found {' '.join(c['dashdash']) or 'nothing'!r}")
    elif intent["verb"] == "port-forward":
        tgt = args[0] if args else ""
        kind, _, name = tgt.partition("/")
        if name != intent["target"] or kind not in intent["target_kinds"]:
            probs.append(f"the target should be `svc/{intent['target']}`, the command uses {tgt!r}")
        if (args[1] if len(args) > 1 else "") != intent["ports"]:
            probs.append(f"the ports should be LOCAL:REMOTE = {intent['ports']}, the command uses {args[1] if len(args) > 1 else 'none'!r}")
    else:
        if intent.get("args_head"):
            n = len(intent["args_head"])
            if args[:n] != intent["args_head"]: probs.append(f"the action should be `{' '.join(intent['args_head'])}`")
            args = args[n:]
        kind, name, extra = kube_target(args)
        want = intent.get("kind")
        if want and KUBE_KIND.get(kind.split(".")[0].lower(), kind) != want:
            probs.append(f"the resource type should be {want}, not {kind!r}")
        if intent.get("name") and name != intent["name"]:
            probs.append(f"the resource name should be `{intent['name']}`, not {name!r}")
    if "namespace" in intent:
        if fl.get("all-namespaces"): probs.append(f"it must be limited to namespace `{intent['namespace']}`, not all namespaces")
        elif fl.get("namespace") != intent["namespace"]:
            probs.append(f"the namespace should be `{intent['namespace']}`, the command uses {fl.get('namespace')!r}")
    if "replicas" in intent and str(fl.get("replicas")) != intent["replicas"]:
        probs.append(f"the replica count should be {intent['replicas']}, the command sets {fl.get('replicas')!r}")
    if intent.get("follow") and fl.get("follow") in (None, False):
        probs.append("it does not follow (stream) the log")
    if "tail" in intent and str(fl.get("tail")) != intent["tail"]:
        probs.append(f"it should show the last {intent['tail']} lines, the command uses tail={fl.get('tail')!r}")
    if "sort_by" in intent:
        got = str(fl.get("sort-by", "")).strip("{}").lstrip(".")
        if got != intent["sort_by"].lstrip("."):
            probs.append("the list is not sorted by the pod creation timestamp" +
                         (f" (sort expression found: {fl['sort-by']!r})" if "sort-by" in fl else " (no sort expression found)"))
    for k, v in intent.get("flags", {}).items():
        got = str(fl.get(k, "")); ok = got.strip("{}").lstrip(".") == v.lstrip(".") if k == "sort-by" else got == v
        if not ok: probs.append(f"the --{k} option should be {v!r}, the command has {fl.get(k)!r}")
    if "jsonpath_has" in intent:
        out = str(fl.get("output", ""))
        if not out.startswith("jsonpath="):
            probs.append(f"the output format should be jsonpath, the command uses {out or 'the default table'!r}")
        elif any(p not in out for p in intent["jsonpath_has"]):
            probs.append(f"the jsonpath expression {out[9:]!r} does not print the node names (it must read " +
                         " and ".join(f"`{p}`" for p in intent["jsonpath_has"]) + ")")
    return probs

def verify_kubectl(answer, intent=None):
    """Parse-check with the real kubectl, offline: no network namespace, dummy kubeconfig, minimal PATH.
    With an `intent` (public task requirements) the parsed command is also checked for meaning."""
    unshare, tmo, kube = shutil.which("unshare"), shutil.which("timeout"), shutil.which("kubectl")
    if not (unshare and tmo and kube): raise SystemExit("kubectl verifier needs unshare, timeout and kubectl")
    blocks = base.code_blocks(answer)
    text = (blocks[0] if blocks else answer).strip().replace("\\\n", " ")
    lines = [l.strip() for l in text.splitlines() if l.strip() and not l.strip().startswith("#")]
    if len(lines) != 1: return False, "reply with exactly one kubectl command"
    try: argv = shlex.split(re.sub(r"^\$\s*", "", lines[0]))
    except ValueError as e: return False, f"the command cannot be parsed: {e}"
    if not argv or argv[0] != "kubectl": return False, "the command must start with kubectl"
    if any(a in ("|", "||", "&&", ";", "&", ">", ">>", "<") or "$(" in a or "`" in a for a in argv):
        return False, "it must be a single kubectl invocation: no pipes, redirects or substitutions"
    with tempfile.TemporaryDirectory() as d:
        open(f"{d}/kc", "w").write("apiVersion: v1\nkind: Config\nclusters:\n- name: x\n  cluster: {server: 'https://127.0.0.1:1'}\n"
                                   "contexts:\n- name: x\n  context: {cluster: x, user: x}\ncurrent-context: x\n"
                                   "users:\n- name: x\n  user: {token: dummy}\n")
        os.mkdir(f"{d}/bin"); os.symlink(kube, f"{d}/bin/kubectl")
        p = subprocess.run([unshare, "-rn", tmo, "15", kube, *argv[1:], "--request-timeout=3s"],
                           env={"PATH": f"{d}/bin", "HOME": d, "KUBECONFIG": f"{d}/kc"}, stdin=subprocess.DEVNULL,
                           capture_output=True, text=True)
    bad = [l for l in p.stderr.splitlines() if re.match(r"[Ee]rror:", l) and not CONN.search(l)]
    if bad or re.search(r"unknown (flag|shorthand flag|command)", p.stderr):
        return False, "kubectl rejected the command: " + (bad[0] if bad else "unknown flag or command")
    if intent:
        probs = kube_intent_problems(argv, intent)
        if probs: return False, "the command is valid kubectl but does not do what was asked: " + "; ".join(probs)
    return True, ""

def verify_sql(q, pub, answer):
    ok, detail = base.sql_check(pub["setup"], pub["expected"], pub.get("ordered", False), answer)
    return ok, "" if ok else f"on a small example table the query {detail}"

def verify_shell(q, pub, answer):
    ok, detail = base.sh_check(pub["files"], pub["expected"], pub.get("post"), answer)
    return ok, "" if ok else f"on a small example the command's {detail}"

def verify(q, answer):
    if q["type"] == "sql": return verify_sql(q, PUBLIC[q["id"]], answer)
    if q["type"] == "shell": return verify_shell(q, PUBLIC[q["id"]], answer)
    if q["type"] == "regex": return verify_regex(q, PUBLIC[q["id"]], answer)
    if q["type"] == "python": return verify_python(q, PUBLIC[q["id"]], answer)
    return verify_kubectl(answer, PUBLIC[q["id"]].get("intent") if KUBECTL_SEMANTIC else None)

# ---------------------------------------------------------------- running
def start_server(spec):
    try:
        urllib.request.urlopen(f"http://localhost:{base.PORT}/health", timeout=2)
        raise SystemExit(f"a server is already answering on port {base.PORT}: refusing to benchmark against an unknown model (stop it first: make stop-all)")
    except OSError: pass
    global SYSTEM; SYSTEM = spec.get("system")
    env = dict(os.environ, LD_LIBRARY_PATH=base.BACKEND)
    cmd = [f"{base.BACKEND}/llama-server", "-m", os.path.expanduser(spec["path"]), "-ngl", "0", "-t", "4",
           "-c", "4096", "--port", str(base.PORT), "--no-webui"] + spec["args"]
    srv = subprocess.Popen(cmd, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(180):
        try: urllib.request.urlopen(f"http://localhost:{base.PORT}/health", timeout=2); return srv
        except Exception:
            if srv.poll() is not None: raise SystemExit("server died on startup")
            time.sleep(2)
    srv.terminate(); raise SystemExit("server did not become healthy")

SYSTEM = None   # optional system prompt from models.json ("system"), set in start_server

def start_messages(q):
    return ([{"role": "system", "content": SYSTEM}] if SYSTEM else []) + [{"role": "user", "content": q["prompt"]}]

def ask(messages, seed):
    t0 = time.time()
    d = base.post({"messages": messages, **base.PARAMS, **SAMPLE, "seed": seed, "cache_prompt": False})
    dt = time.time() - t0
    m, n = d["choices"][0]["message"], d["usage"]["completion_tokens"]
    return (m.get("content") or ""), n, dt, d["choices"][0]["finish_reason"], len(m.get("reasoning_content") or "")

def run_question(name, mode, seed, q, retries):
    messages = start_messages(q)
    attempts = []
    for i in range(1 + (retries if mode == "harness" else 0)):
        ans, n, dt, fin, rchars = ask(messages, seed)
        ok, detail = base.check(q, ans)
        rec = {"answer": ans, "tokens": n, "seconds": round(dt, 1), "tps": round(n / dt, 2), "finish_reason": fin,
               "hidden_pass": ok, "hidden_detail": detail, "verifier_pass": None, "verifier_feedback": "", "reasoning_chars": rchars}
        if mode == "harness":
            rec["verifier_pass"], rec["verifier_feedback"] = verify(q, ans)
        attempts.append(rec)
        if mode != "harness" or rec["verifier_pass"] or i == retries: break
        messages += [{"role": "assistant", "content": ans},
                     {"role": "user", "content": f"That answer failed verification: {rec['verifier_feedback']}\n"
                                                 f"Fix it. Reply with ONLY the corrected {ASK[q['type']]} in a code block."}]
    meta = {"model": name, "mode": mode, "seed": seed, "question": q["id"], "category": q["category"],
            "first_pass": attempts[0]["hidden_pass"], "final_pass": attempts[-1]["hidden_pass"],
            "retried": len(attempts) > 1, "sampling": {**base.PARAMS, **SAMPLE, "seed": seed, "profile": PROFILE}, "tokens_total": sum(a["tokens"] for a in attempts),
            "seconds_total": round(sum(a["seconds"] for a in attempts), 1),
            "attempts": [{k: v for k, v in a.items() if k != "answer"} for a in attempts]}
    d = f"{RUNS}/{mode}/{name}/seed{seed}"
    os.makedirs(d, exist_ok=True)
    json.dump(meta, open(f"{d}/{q['id']}.json", "w"), indent=1)
    with open(f"{d}/{q['id']}.md", "w") as f:
        f.write(f"# {name} / {q['id']} / seed {seed} / {mode}\n\n## Prompt\n\n{q['prompt']}\n")
        for i, a in enumerate(attempts, 1):
            f.write(f"\n## Attempt {i}: {'PASS' if a['hidden_pass'] else 'FAIL'} (hidden: {a['hidden_detail']})\n\n"
                    f"- {a['tokens']} tokens in {a['seconds']}s, finish: {a['finish_reason']}\n")
            if a["verifier_pass"] is not None:
                f.write(f"- verifier: {'pass' if a['verifier_pass'] else 'FAIL: ' + a['verifier_feedback']}\n")
            f.write(f"\n{a['answer']}\n")
    return meta

def first_answer(name, seed, qid):
    """First attempt of a saved harness cell: its record and its answer text."""
    d = f"{RUNS}/harness/{name}/seed{seed}"
    m = json.load(open(f"{d}/{qid}.json")); md = open(f"{d}/{qid}.md").read()
    bodies = [re.sub(r"\A(\n?- [^\n]*\n)+", "", b) for b in re.split(r"\n## Attempt \d+:[^\n]*\n", md)[1:]]
    return m, dict(m["attempts"][0], answer=bodies[0].strip("\n"))

def run_resample(name, seed, q, retries):
    """Control arm: same trigger as the harness (verifier rejects), but the retry is a fresh sample of the original prompt
    with a new seed and NO feedback. First attempts are reused from the harness run (same seed, identical)."""
    h, first = first_answer(name, seed, q["id"])
    attempts = [first]
    messages = start_messages(q)
    for i in range(1, retries + 1):
        if attempts[-1]["verifier_pass"]: break
        ans, n, dt, fin, rchars = ask(messages, seed + 1000 * i)
        ok, detail = base.check(q, ans)
        vp, vf = verify(q, ans)
        attempts.append({"answer": ans, "tokens": n, "seconds": round(dt, 1), "tps": round(n / dt, 2), "finish_reason": fin,
                         "hidden_pass": ok, "hidden_detail": detail, "verifier_pass": vp, "verifier_feedback": vf, "reasoning_chars": rchars,
                         "retry_seed": seed + 1000 * i})
    meta = {"model": name, "mode": "resample", "seed": seed, "question": q["id"], "category": q["category"],
            "first_pass": attempts[0]["hidden_pass"], "final_pass": attempts[-1]["hidden_pass"], "retried": len(attempts) > 1,
            "sampling": {**base.PARAMS, **SAMPLE, "seed": seed, "profile": PROFILE}, "tokens_total": sum(a["tokens"] for a in attempts),
            "seconds_total": round(sum(a["seconds"] for a in attempts), 1),
            "attempts": [{k: v for k, v in a.items() if k != "answer"} for a in attempts]}
    d = f"{RUNS}/resample/{name}/seed{seed}"
    os.makedirs(d, exist_ok=True)
    json.dump(meta, open(f"{d}/{q['id']}.json", "w"), indent=1)
    with open(f"{d}/{q['id']}.md", "w") as f:
        f.write(f"# {name} / {q['id']} / seed {seed} / resample (no feedback)\n\n## Prompt\n\n{q['prompt']}\n")
        for i, a in enumerate(attempts, 1):
            f.write(f"\n## Attempt {i}: {'PASS' if a['hidden_pass'] else 'FAIL'} (hidden: {a['hidden_detail']})\n\n"
                    f"- {a['tokens']} tokens in {a['seconds']}s, finish: {a['finish_reason']}\n"
                    f"- verifier: {'pass' if a['verifier_pass'] else 'FAIL: ' + a['verifier_feedback']}\n\n{a['answer']}\n")
    return meta

def conditions():
    mi = dict(l.split(":")[0:2] for l in open("/proc/meminfo").read().splitlines())
    kb = lambda k: int(mi[k].split()[0]) // 1024
    return {"time": time.strftime("%Y-%m-%d %H:%M:%S"), "sampling_profile": PROFILE, "sampling": {**base.PARAMS, **SAMPLE}, "mem_available_mb": kb("MemAvailable"),
            "swap_used_mb": kb("SwapTotal") - kb("SwapFree"), "loadavg_1m": round(os.getloadavg()[0], 2),
            "uptime_min": round(float(open("/proc/uptime").read().split()[0]) / 60)}

def run_batch(a):
    models = json.load(open(f"{HERE}/models.json"))
    questions = json.load(open(f"{HERE}/questions.json"))
    if a.questions: questions = [q for q in questions if q["id"] in a.questions.split(",")]
    seeds = [int(s) for s in a.seeds.split(",")]
    for name in (a.models.split(",") if a.models else list(models)):
        todo = [(s, q) for s in seeds for q in questions
                if a.force or not os.path.exists(f"{RUNS}/{a.mode}/{name}/seed{s}/{q['id']}.json")]
        if not todo: print(f"[{name}] nothing to do"); continue
        os.makedirs(f"{RUNS}/{a.mode}/{name}", exist_ok=True)
        SAMPLE.clear(); SAMPLE.update(models[name].get("sampling", {}).get(a.sampling, {}) if a.sampling != "default" else {})
        if a.sampling != "default" and not SAMPLE and not over: print(f"[{name}] no '{a.sampling}' profile in models.json, skipped"); continue
        SAMPLE.update({k.replace("-", "_"): v for k, v in over.items()})
        json.dump(conditions(), open(f"{RUNS}/{a.mode}/{name}/conditions.json", "w"), indent=1)
        srv = start_server(models[name])
        try:
            for s, q in todo:
                m = run_resample(name, s, q, a.retries) if a.mode == "resample" else run_question(name, a.mode, s, q, a.retries)
                last = m["attempts"][-1]
                print(f"[{name}] seed {s} {q['id']:20} first={'PASS' if m['first_pass'] else 'FAIL'} "
                      f"final={'PASS' if m['final_pass'] else 'FAIL'} tries={len(m['attempts'])} "
                      f"{m['tokens_total']:4d} tok {m['seconds_total']:5.1f}s", flush=True)
        finally:
            srv.terminate(); srv.wait()

# ---------------------------------------------------------------- statistics
def load(mode, name, root=None):
    runs = {}
    for p in sorted(glob.glob(f"{root or RUNS}/{mode}/{name}/seed*/*.json")):
        m = json.load(open(p)); runs.setdefault(m["seed"], {})[m["question"]] = m
    return runs

def ms(xs):
    return f"{st.mean(xs):.1f} ± {st.stdev(xs):.1f}" if len(xs) > 1 else f"{xs[0]:.1f}"

def naked_view(name):
    """(source, {seed: {question: passed, tps}}) from a naked run, else from harness first attempts."""
    runs, src = load("naked", name), "naked"
    if not runs: runs, src = load("harness", name), "harness first attempt"
    return src, {s: {q: {"pass": m["attempts"][0]["hidden_pass"], "tps": m["attempts"][0]["tps"],
                         "cat": m["category"]} for q, m in qs.items()} for s, qs in runs.items()}

def stats(questions):
    names = sorted({p.split(os.sep)[-2] for p in glob.glob(f"{RUNS}/*/*/conditions.json")})
    qids = [q["id"] for q in questions]
    cats = sorted({q["category"] for q in questions})
    out = ["# Repeated-run statistics\n"]
    for mode in ("naked", "harness"):
        for p in sorted(glob.glob(f"{RUNS}/{mode}/*/conditions.json")):
            c = json.load(open(p))
            out.append(f"- {mode} / {p.split(os.sep)[-2]}: started {c['time']}, uptime {c['uptime_min']} min, "
                       f"{c['mem_available_mb']} MB available, swap used {c['swap_used_mb']} MB, load {c['loadavg_1m']}")
    out += ["", "## A. Stability, no harness (first attempt, one run per seed)\n",
            "| Model (source) | Seeds | Score per seed | Mean ± SD | Range | Always pass | Never pass | Flaky | Best-of-runs | Speed t/s (mean ± SD of runs) |",
            "|---|---:|---|---|---|---:|---:|---:|---:|---|"]
    views = {n: naked_view(n) for n in names}
    for n in names:
        src, v = views[n]
        if not v: continue
        seeds = sorted(v)
        tot = [sum(v[s][q]["pass"] for q in qids if q in v[s]) for s in seeds]
        per_q = {q: [v[s][q]["pass"] for s in seeds if q in v[s]] for q in qids}
        always = sum(all(x) for x in per_q.values()); never = sum(not any(x) for x in per_q.values())
        flaky = len(qids) - always - never; best = sum(any(x) for x in per_q.values())
        tps = [st.mean(v[s][q]["tps"] for q in v[s]) for s in seeds]
        out.append(f"| {n} ({src}) | {len(seeds)} | {' / '.join(f'{t}/{len(qids)}' for t in tot)} | {ms(tot)} | "
                   f"{min(tot)}-{max(tot)} | {always} | {never} | {flaky} | {best}/{len(qids)} | {ms(tps)} |")
    out += ["", "Per category (mean pass count over seeds, out of the category size):\n",
            "| Model | " + " | ".join(f"{c} ({sum(q['category'] == c for q in questions)})" for c in cats) + " |",
            "|---|" + "---:|" * len(cats)]
    for n in names:
        v = views[n][1]
        if v: out.append(f"| {n} | " + " | ".join(
            ms([sum(r["pass"] for r in v[s].values() if r["cat"] == c) for s in sorted(v)]) for c in cats) + " |")
    out += ["", "### Per question: passes / runs (`*` = flaky, i.e. the model gave different outcomes across seeds)\n",
            "| Question | " + " | ".join(n for n in names if views[n][1]) + " |",
            "|---|" + "---|" * sum(bool(views[n][1]) for n in names)]
    for q in qids:
        row = []
        for n in names:
            v = views[n][1]
            if not v: continue
            x = [v[s][q]["pass"] for s in sorted(v) if q in v[s]]
            row.append(f"{sum(x)}/{len(x)}" + ("*" if 0 < sum(x) < len(x) else "") if x else "-")
        out.append(f"| {q} | " + " | ".join(row) + " |")
    hm = [n for n in names if load("harness", n)]
    if hm:
        at = lambda m, k: m["attempts"][min(k, len(m["attempts"]) - 1)]["hidden_pass"]   # result after k retries
        out += ["", "## B. Harness: generate -> verify (public examples / offline kubectl parser) -> retry with feedback\n",
                "Score = hidden-test passes out of %d, per seed, then mean ± SD over seeds.\n" % len(qids),
                "| Model | No harness | +1 retry | +2 retries | Answers rejected by verifier per run | Fixed by retry | Broken by retry | "
                "Verifier OK but hidden test failed | Time cost |", "|---|---|---|---|---|---:|---:|---:|---|"]
        for n in hm:
            runs = load("harness", n); seeds = sorted(runs)
            sc = {k: [sum(at(m, k) for m in runs[s].values()) for s in seeds] for k in (0, 1, 2)}
            rej = [sum(m["retried"] for m in runs[s].values()) for s in seeds]
            allm = [m for s in seeds for m in runs[s].values()]
            fixed = sum(not m["first_pass"] and m["final_pass"] for m in allm)
            broke = sum(m["first_pass"] and not m["final_pass"] for m in allm)
            false_ok = sum(bool(m["attempts"][-1]["verifier_pass"]) and not m["final_pass"] for m in allm)
            t0 = sum(m["attempts"][0]["seconds"] for m in allm); t1 = sum(m["seconds_total"] for m in allm)
            cell = lambda k: f"{ms(sc[k])} ({' / '.join(map(str, sc[k]))})"
            out.append(f"| {n} | {cell(0)} | {cell(1)} | {cell(2)} | {ms(rej)} | {fixed} | {broke} | {false_ok} | x{t1 / t0:.2f} |")
        out += ["", "### Per question: passes without harness -> +1 retry -> +2 retries (over the same seeds)\n",
                "| Question | " + " | ".join(hm) + " |", "|---|" + "---|" * len(hm)]
        for q in qids:
            row = []
            for n in hm:
                runs = load("harness", n); ms_ = [runs[s][q] for s in sorted(runs) if q in runs[s]]
                row.append(" -> ".join(f"{sum(at(m, k) for m in ms_)}/{len(ms_)}" for k in (0, 1, 2)) if ms_ else "-")
            out.append(f"| {q} | " + " | ".join(row) + " |")
    def answers(path):
        """First code block (or the text) of every attempt in a transcript."""
        res = []
        for body in re.split(r"\n## Attempt \d+:[^\n]*\n", open(path).read())[1:]:
            body = re.sub(r"\A(\n?- [^\n]*\n)+", "", body)
            b = base.code_blocks(body)
            res.append((b[0] if b else body).strip())
        return res

    if hm:
        out += ["", "## C. Retry behaviour\n",
                "| Model | Retries issued | Retry returned the same code block unchanged | Retries that passed the hidden tests | "
                "Mean tokens: first attempt / retry | Attempts that hit the token cap | Longest attempt (tokens) |",
                "|---|---:|---:|---:|---|---:|---:|"]
        for n in hm:
            runs = load("harness", n)
            issued = same = ok = capped = 0; t_first, t_retry, longest = [], [], 0
            for s in runs:
                for q, m in runs[s].items():
                    ans = answers(f"{RUNS}/harness/{n}/seed{s}/{q}.md")
                    for i, a in enumerate(m["attempts"]):
                        capped += a["finish_reason"] == "length"; longest = max(longest, a["tokens"])
                        (t_first if i == 0 else t_retry).append(a["tokens"])
                        if i:
                            issued += 1; ok += a["hidden_pass"]; same += ans[i] == ans[i - 1]
            out.append(f"| {n} | {issued} | {same} | {ok} | {st.mean(t_first):.0f} / "
                       f"{(f'{st.mean(t_retry):.0f}' if t_retry else '-')} | {capped} | {longest} |")

    out += ["", "## D. Reproducibility of section 5 (seed 42 here vs the single run in REPORT.md section 5)\n",
            "| Model | Same pass/fail outcome | Differing questions |", "|---|---:|---|"]
    for n in names:
        v = views[n][1]; old = {os.path.basename(p)[:-5]: json.load(open(p))["passed"]
                                for p in glob.glob(f"{HERE}/results/{n}/*.json")}
        if 42 not in v or not old: continue
        diff = [f"{q} ({'pass' if old[q] else 'fail'} -> {'pass' if v[42][q]['pass'] else 'fail'})"
                for q in qids if q in old and q in v[42] and old[q] != v[42][q]["pass"]]
        out.append(f"| {n} | {len(qids) - len(diff)}/{len(qids)} | {', '.join(diff) or 'none'} |")

    both = [n for n in names if load("naked", n) and load("harness", n)]
    if both:
        out += ["", "## E. Determinism: naked run vs first harness attempt (same seed, same request)\n",
                "| Model | Identical answers | Same pass/fail outcome | Cells compared |", "|---|---:|---:|---:|"]
        for n in both:
            a_, b_ = load("naked", n), load("harness", n); same = out_same = tot = 0
            for s in a_:
                for q in a_[s]:
                    if s in b_ and q in b_[s]:
                        tot += 1
                        same += answers(f"{RUNS}/naked/{n}/seed{s}/{q}.md")[0] == answers(f"{RUNS}/harness/{n}/seed{s}/{q}.md")[0]
                        out_same += a_[s][q]["first_pass"] == b_[s][q]["first_pass"]
            out.append(f"| {n} | {same}/{tot} | {out_same}/{tot} | {tot} |")
    open(f"{RUNS}/STATS.md", "w").write("\n".join(out) + "\n")
    print("\n".join(out))

def regrade_runs(questions):
    """Re-run the hidden grader on every saved attempt (no model needed); prints the cells that changed."""
    Q = {q["id"]: q for q in questions}
    changed = []
    for p in sorted(glob.glob(f"{RUNS}/*/*/seed*/*.json")):
        m = json.load(open(p)); md = open(p[:-5] + ".md").read()
        bodies = [re.sub(r"\A(\n?- [^\n]*\n)+", "", b) for b in re.split(r"\n## Attempt \d+:[^\n]*\n", md)[1:]]
        for i, (a, body) in enumerate(zip(m["attempts"], bodies), 1):
            ok, detail = base.check(Q[m["question"]], body)
            if ok != a["hidden_pass"]:
                changed.append(f"{m['mode']}/{m['model']}/seed{m['seed']}/{m['question']} attempt {i}: "
                               f"{'pass' if a['hidden_pass'] else 'fail'} -> {'pass' if ok else 'fail'}")
            a["hidden_pass"], a["hidden_detail"] = ok, detail
        m["first_pass"], m["final_pass"] = m["attempts"][0]["hidden_pass"], m["attempts"][-1]["hidden_pass"]
        json.dump(m, open(p, "w"), indent=1)
        n = iter(m["attempts"])
        def head(mo):
            a = next(n); i = int(mo.group(1))
            return f"\n## Attempt {i}: {'PASS' if a['hidden_pass'] else 'FAIL'} (hidden: {a['hidden_detail']})\n"
        open(p[:-5] + ".md", "w").write(re.sub(r"\n## Attempt (\d+): (?:PASS|FAIL) \(hidden: [^\n]*\)\n", head, md))
    print(f"{len(changed)} attempt(s) changed:", *changed, sep="\n  ")

def compare_sampling(profile, questions):
    """Default-sampling runs (runs/) against a sampling profile (runs-<profile>/): same models, seeds, questions, verifier."""
    other = os.path.join(HERE, f"runs-{profile}")
    qids = [q["id"] for q in questions]; cats = sorted({q["category"] for q in questions})
    names = sorted(n for n in {p.split(os.sep)[-2] for p in glob.glob(f"{other}/harness/*/conditions.json")} if load("harness", n))
    out = [f"# Sampling comparison: default benchmark settings vs profile `{profile}`\n",
           "Both sides: harness mode (first attempt = no harness, final after two retries), seeds 42/43/44, same verifier. Score = hidden-test passes out of 11.\n",
           "| Model | Sampling used (default -> profile) | No harness: default | No harness: profile | +2 retries: default | +2 retries: profile | Speed t/s default -> profile |",
           "|---|---|---|---|---|---|---|"]
    detail = []
    for n in names:
        a, b = load("harness", n), load("harness", n, other); seeds = sorted(set(a) & set(b))
        cond = json.load(open(f"{other}/harness/{n}/conditions.json")).get("sampling", {})
        keys = ("temperature", "top_p", "top_k", "min_p", "repeat_penalty", "presence_penalty")
        sa = "T0.6 top_p0.95 top_k20 min_p0.05* rep1.0"
        sb = f"T{cond.get('temperature')} top_p{cond.get('top_p')} top_k{cond.get('top_k')} min_p{cond.get('min_p')} rep{cond.get('repeat_penalty')}"
        first = lambda r, s: sum(r[s][q]["attempts"][0]["hidden_pass"] for q in qids if q in r[s])
        final = lambda r, s: sum(r[s][q]["final_pass"] for q in qids if q in r[s])
        tps = lambda r: st.mean(m["attempts"][0]["tps"] for s in seeds for m in r[s].values())
        f0, f1 = [first(a, s) for s in seeds], [first(b, s) for s in seeds]
        g0, g1 = [final(a, s) for s in seeds], [final(b, s) for s in seeds]
        out.append(f"| {n} | {sa} -> {sb} | {ms(f0)} ({' / '.join(map(str, f0))}) | {ms(f1)} ({' / '.join(map(str, f1))}) | "
                   f"{ms(g0)} ({' / '.join(map(str, g0))}) | {ms(g1)} ({' / '.join(map(str, g1))}) | {tps(a):.1f} -> {tps(b):.1f} |")
        rows = []
        for q in qids:
            x = [a[s][q]["attempts"][0]["hidden_pass"] for s in seeds if q in a[s]]
            y = [b[s][q]["attempts"][0]["hidden_pass"] for s in seeds if q in b[s]]
            x2 = [a[s][q]["final_pass"] for s in seeds if q in a[s]]; y2 = [b[s][q]["final_pass"] for s in seeds if q in b[s]]
            rows.append((q, sum(x), sum(y), sum(x2), sum(y2)))
        detail.append((n, rows))
        cat = lambda r, c: ms([sum(r[s][q]["attempts"][0]["hidden_pass"] for q in qids if q in r[s] and r[s][q]["category"] == c) for s in seeds])
        out.append("")
    out.append("`*` = llama-server's built-in default `min_p` 0.05, which the benchmark never overrode (see REPORT.md 6.10).\n")
    out += ["## Per question: passes out of 3 seeds, default -> profile (no harness; in brackets after 2 retries)\n",
            "| Question | " + " | ".join(names) + " |", "|---|" + "---|" * len(names)]
    for i, q in enumerate(qids):
        cells = []
        for n, rows in detail:
            _, x, y, x2, y2 = rows[i]
            mark = "" if (x, x2) == (y, y2) else " **changed**"
            cells.append(f"{x} -> {y} (retries: {x2} -> {y2}){mark}")
        out.append(f"| {q} | " + " | ".join(cells) + " |")
    out += ["", "## Per category: mean passes per seed, no harness, default -> profile\n",
            "| Model | " + " | ".join(f"{c} ({sum(q['category'] == c for q in questions)})" for c in cats) + " |", "|---|" + "---:|" * len(cats)]
    for n in names:
        a, b = load("harness", n), load("harness", n, other); seeds = sorted(set(a) & set(b))
        cells = []
        for c in cats:
            f = lambda r: ms([sum(r[s][q]["attempts"][0]["hidden_pass"] for q in qids if q in r[s] and r[s][q]["category"] == c) for s in seeds])
            cells.append(f"{f(a)} -> {f(b)}")
        out.append(f"| {n} | " + " | ".join(cells) + " |")
    open(f"{other}/COMPARE.md", "w").write("\n".join(out) + "\n")
    print("\n".join(out))

def resample_summary(questions):
    """Harness (retry with feedback) vs control (fresh sample, no feedback), same trigger and seeds; writes runs/RESAMPLE.md."""
    out = ["# Control arm: retry with feedback vs retry without feedback (fresh sample, new seed)", "",
           "Same first attempts, same verifier trigger, up to 2 retries; hidden tests grade. Score /11, mean ± SD over seeds 42/43/44.", "",
           "| Model | No retry | + 2 retries WITH feedback (harness) | + 2 retries WITHOUT feedback (control) | Cells fixed: feedback / no feedback | Cells broken: feedback / no feedback |",
           "|---|---|---|---|---|---|"]
    tot = [0, 0, 0, 0]; cat = {"code": [0, 0], "kubectl": [0, 0]}
    for name in sorted(os.listdir(f"{RUNS}/resample")) if os.path.isdir(f"{RUNS}/resample") else []:
        H, R = load("harness", name), load("resample", name)
        seeds = sorted(s for s in R if len(R[s]) == len(questions))
        if not seeds: continue
        f = lambda D, key: [sum(D[s][q["id"]][key] for q in questions) for s in seeds]
        first, hf, rf = f(H, "first_pass"), f(H, "final_pass"), f(R, "final_pass")
        fx = lambda D: sum(D[s][q["id"]]["final_pass"] and not D[s][q["id"]]["first_pass"] for s in seeds for q in questions)
        bk = lambda D: sum(D[s][q["id"]]["first_pass"] and not D[s][q["id"]]["final_pass"] for s in seeds for q in questions)
        for s in seeds:
            for q in questions:
                c = "kubectl" if q["category"] == "kubectl" else "code"
                cat[c][0] += H[s][q["id"]]["final_pass"] and not H[s][q["id"]]["first_pass"]
                cat[c][1] += R[s][q["id"]]["final_pass"] and not R[s][q["id"]]["first_pass"]
        tot[0] += fx(H); tot[1] += fx(R); tot[2] += bk(H); tot[3] += bk(R)
        cell = lambda xs: f"{ms(xs)} ({' / '.join(map(str, xs))})"
        out.append(f"| {name} | {cell(first)} | {cell(hf)} | {cell(rf)} | {fx(H)} / {fx(R)} | {bk(H)} / {bk(R)} |")
    out += ["", f"All models: cells fixed {tot[0]} with feedback vs {tot[1]} without; cells broken {tot[2]} vs {tot[3]}.",
            f"By type (fixed with / without feedback): regex+Python {cat['code'][0]} / {cat['code'][1]}, kubectl {cat['kubectl'][0]} / {cat['kubectl'][1]}."]
    open(f"{RUNS}/RESAMPLE.md", "w").write("\n".join(out) + "\n"); print("\n".join(out))

def kubectl_replay(questions):
    """Replay saved kubectl answers (naked + harness, every attempt) through the old and new verifier; compare with the hidden grade."""
    Q = {q["id"]: q for q in questions if q["category"] == "kubectl"}
    seen = {}
    for p in sorted(glob.glob(f"{RUNS}/*/*/seed*/kubectl-*.json")):
        m = json.load(open(p)); md = open(p[:-5] + ".md").read()
        bodies = [re.sub(r"\A(\n?- [^\n]*\n)+", "", b) for b in re.split(r"\n## Attempt \d+:[^\n]*\n", md)[1:]]
        for a, body in zip(m["attempts"], bodies):
            seen.setdefault((m["question"], body.strip()), a["hidden_pass"])
    rows = []
    for (qid, body), hidden in seen.items():
        old = verify_kubectl(body)[0]; new_ok, why = verify_kubectl(body, PUBLIC[qid]["intent"])
        rows.append((qid, body, hidden, old, new_ok, why))
    print(f"{len(rows)} distinct kubectl answers")
    print(f"{'question':22} {'n':>3} | old verifier: ok&hidden-fail  rejects-good | new verifier: ok&hidden-fail  rejects-good")
    for qid in Q:
        r = [x for x in rows if x[0] == qid]
        f = lambda i: (sum(x[i] and not x[2] for x in r), sum((not x[i]) and x[2] for x in r))
        print(f"{qid:22} {len(r):3d} | {f(3)[0]:>24} {f(3)[1]:>14} | {f(4)[0]:>24} {f(4)[1]:>14}")
    print("\nNew verifier disagrees with the hidden grade:")
    for qid, body, hidden, old, new_ok, why in rows:
        if new_ok != hidden:
            print(f"- {qid}: hidden={'pass' if hidden else 'FAIL'}, verifier={'ok' if new_ok else 'REJECT'}  {why[:150]}\n    {body.splitlines()[-1][:140] if body else ''}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["naked", "harness", "resample"], default="naked")
    ap.add_argument("-m", "--models"); ap.add_argument("-q", "--questions")
    ap.add_argument("--seeds", default="42,43,44"); ap.add_argument("--retries", type=int, default=2)
    ap.add_argument("--force", action="store_true"); ap.add_argument("--stats", action="store_true")
    ap.add_argument("--regrade", action="store_true"); ap.add_argument("--kubectl-replay", action="store_true")
    ap.add_argument("--sampling", default="default", help="profile from models.json 'sampling' (per model), e.g. vendor; default = benchmark settings")
    ap.add_argument("--tag", help="results folder suffix for command-line overrides (runs-<tag>/); defaults to the profile name")
    for k in ("temperature", "top-p", "top-k", "min-p", "repeat-penalty", "presence-penalty"):
        ap.add_argument(f"--{k}", type=float if k not in ("top-k",) else int)
    ap.add_argument("--compare", metavar="PROFILE", help="compare runs-PROFILE/ with the default runs/")
    a = ap.parse_args()
    over = {k: getattr(a, k.replace("-", "_")) for k in ("temperature", "top-p", "top-k", "min-p", "repeat-penalty", "presence-penalty")
            if getattr(a, k.replace("-", "_")) is not None}
    if a.sampling != "default" or over:
        PROFILE = a.tag or (a.sampling if a.sampling != "default" else None)
        if not PROFILE: raise SystemExit("sampling overrides on the command line need --tag NAME (results go to runs-NAME/)")
        RUNS = os.path.join(HERE, f"runs-{PROFILE}")
    if a.compare: compare_sampling(a.compare, json.load(open(f"{HERE}/questions.json"))); raise SystemExit
    if a.kubectl_replay: kubectl_replay(json.load(open(f"{HERE}/questions.json")))
    elif a.regrade: regrade_runs(json.load(open(f"{HERE}/questions.json"))); stats(json.load(open(f"{HERE}/questions.json")))
    elif a.stats: stats(json.load(open(f"{HERE}/questions.json")))
    elif a.mode == "resample":
        run_batch(a); resample_summary(json.load(open(f"{HERE}/questions.json")))
    else:
        run_batch(a)
        stats(json.load(open(f"{HERE}/questions.json")))
