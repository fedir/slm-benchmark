#!/usr/bin/env python3
"""Throughput measurements with repetitions (run on a QUIET machine, one server at a time).

  speed.py                 run every configuration below, write benchmarks/speed/SPEED.md and speed.json
  speed.py -c qwen3b       only configurations whose name contains the text
  speed.py --reps 7        repetitions per configuration (default 7; the first, warm-up request is discarded)

For each configuration: start llama-server, one warm-up request, then N timed requests with the same ~300-token prompt and 128 generated tokens
(greedy: temperature 0, so every repetition does the same work), cache_prompt off so prefill is measured every time. Prompt-processing and
generation speed are read from the server's own `timings` (prompt_per_second, predicted_per_second); MTP acceptance from draft_n / draft_n_accepted.
Reports mean ± SD and a bandwidth ceiling check (effective GB/s = file size x generation t/s).
"""
import argparse, glob, json, os, statistics as st, subprocess, sys, time, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import run as base

OUT = os.path.join(HERE, "speed")
M = json.load(open(f"{HERE}/models.json"))
ORNITH_STOCK = "{MODELS_DIR}/ornith-ai/Ornith-1.5-9B-GGUF/Ornith-1.5-9B-Q4_K_M.gguf"
PROMPT = ("Review the following Python function and explain, in about 100 words, what it does, whether it is correct and how you would improve it.\n\n"
          + "def merge_intervals(intervals):\n    intervals.sort(key=lambda x: x[0])\n    merged = []\n    for start, end in intervals:\n"
          "        if merged and start <= merged[-1][1]:\n            merged[-1][1] = max(merged[-1][1], end)\n        else:\n            merged.append([start, end])\n    return merged\n\n"
          "The function is used on lists of up to a million [start, end] pairs coming from log files; some entries may be unsorted, some may touch, "
          "and some may be nested inside others. The team also wonders whether sorting in place is a problem for callers that reuse the list, "
          "whether an empty input is handled, and whether integers and floats can be mixed. Answer in plain prose without code. ") * 1

def configs():
    c = []
    for name, spec in M.items():
        c.append((f"{name}/cpu-t4", spec["path"], spec["args"], ["-ngl", "0", "-t", "4"]))
        c.append((f"{name}/cpu-t8", spec["path"], spec["args"], ["-ngl", "0", "-t", "8"]))
    for t in (2, 3, 6):
        c.append((f"qwen2.5-coder-3b/cpu-t{t}", M["qwen2.5-coder-3b"]["path"], [], ["-ngl", "0", "-t", str(t)]))
    for name in ("qwen2.5-coder-3b", "ornith-9b-mtp", "nemotron-3-nano-4b"):
        c.append((f"{name}/vulkan-all-layers", M[name]["path"], M[name]["args"], ["-ngl", "99", "-t", "4"]))
    p = M["ornith-9b-mtp"]["path"]
    c.append(("ornith/stock-gguf-no-spec", ORNITH_STOCK, [], ["-ngl", "0", "-t", "4"]))
    c.append(("ornith/mtp-gguf-no-spec", p, [], ["-ngl", "0", "-t", "4"]))
    for n in (1, 2, 3, 4):
        c.append((f"ornith/mtp-draft{n}", p, ["--spec-type", "draft-mtp", "--spec-draft-n-max", str(n)], ["-ngl", "0", "-t", "4"]))
    c.append(("qwen2.5-coder-3b/cpu-t4-flash-attn", M["qwen2.5-coder-3b"]["path"], ["-fa", "on"], ["-ngl", "0", "-t", "4"]))
    c.append(("qwen2.5-coder-3b/cpu-t4-no-mmap", M["qwen2.5-coder-3b"]["path"], ["--no-mmap"], ["-ngl", "0", "-t", "4"]))
    return c

def request():
    t0 = time.time()
    d = base.post({"messages": [{"role": "user", "content": PROMPT}], "max_tokens": 128, "temperature": 0, "top_k": 1, "seed": 1,
                   "cache_prompt": False, "chat_template_kwargs": {"enable_thinking": False}})
    t = d["timings"]
    return {"prompt_n": t["prompt_n"], "prompt_tps": t["prompt_per_second"], "gen_n": t["predicted_n"], "gen_tps": t["predicted_per_second"],
            "draft_n": t.get("draft_n", 0), "draft_ok": t.get("draft_n_accepted", 0), "wall": round(time.time() - t0, 2)}

def measure(name, path, args, hw, reps):
    try:
        urllib.request.urlopen(f"http://localhost:{base.PORT}/health", timeout=2)
        raise SystemExit(f"a server is already answering on port {base.PORT}; stop it first")
    except OSError: pass
    path = base.expand(path)
    env = dict(os.environ, LD_LIBRARY_PATH=base.BACKEND)
    srv = subprocess.Popen([f"{base.BACKEND}/llama-server", "-m", path, *hw, "-c", "4096", "--port", str(base.PORT), "--no-webui", *[base.expand(x) for x in args]],
                           env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        for _ in range(240):
            try: urllib.request.urlopen(f"http://localhost:{base.PORT}/health", timeout=2); break
            except Exception:
                if srv.poll() is not None: return {"name": name, "error": "server died on startup"}
                time.sleep(2)
        else: return {"name": name, "error": "server did not become healthy"}
        request()                                         # warm-up (page cache, kernels), discarded
        runs = [request() for _ in range(reps)]
        mi = dict(l.split(":")[0:2] for l in open("/proc/meminfo").read().splitlines())
        return {"name": name, "file_gb": round(os.path.getsize(path) / 1e9, 2), "args": args, "hw": hw, "runs": runs,
                "swap_used_mb": (int(mi["SwapTotal"].split()[0]) - int(mi["SwapFree"].split()[0])) // 1024,
                "mem_available_mb": int(mi["MemAvailable"].split()[0]) // 1024, "loadavg_before": round(os.getloadavg()[0], 2)}
    finally:
        srv.terminate(); srv.wait()

def table(results):
    def ms(xs): return f"{st.mean(xs):.2f} ± {st.stdev(xs):.2f}" if len(xs) > 1 else f"{xs[0]:.2f}"
    lines = ["# Throughput (server timings, greedy, 128 generated tokens, cache_prompt off)", "",
             "Mean ± SD over the timed repetitions (warm-up discarded). Effective bandwidth = file size x generation t/s (the whole model is read once per token; "
             "with speculative decoding it can exceed the true memory traffic per token). Draft acceptance = accepted / drafted tokens.", "",
             "| Configuration | file GB | n | prefill t/s | generation t/s | effective GB/s | draft acceptance | swap MB |", "|---|---|---|---|---|---|---|---|"]
    for r in results:
        if "error" in r: lines.append(f"| {r['name']} | | | | {r['error']} | | | |"); continue
        g = [x["gen_tps"] for x in r["runs"]]; p = [x["prompt_tps"] for x in r["runs"]]
        dn = sum(x["draft_n"] for x in r["runs"]); dk = sum(x["draft_ok"] for x in r["runs"])
        lines.append(f"| {r['name']} | {r['file_gb']} | {len(g)} | {ms(p)} | {ms(g)} | {r['file_gb'] * st.mean(g):.1f} | {f'{100 * dk / dn:.0f}%' if dn else '-'} | {r['swap_used_mb']} |")
    return "\n".join(lines) + "\n"

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("-c", "--only"); ap.add_argument("--reps", type=int, default=7); a = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)
    path = f"{OUT}/speed.json"; results = json.load(open(path)) if os.path.exists(path) else []
    done = {r["name"] for r in results}
    for name, mp, args, hw in configs():
        if (a.only and a.only not in name) or name in done: continue
        print(f"[{name}]", flush=True); r = measure(name, mp, args, hw, a.reps); results.append(r)
        print("   ", r.get("error") or f"gen {st.mean(x['gen_tps'] for x in r['runs']):.2f} t/s", flush=True)
        json.dump(results, open(path, "w"), indent=1)
        open(f"{OUT}/SPEED.md", "w").write(table(results))
    print(table(results))
