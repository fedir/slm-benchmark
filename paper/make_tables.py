#!/usr/bin/env python3
"""Generate LaTeX macros and tables for the paper from the saved data (no number is typed by hand).

  python3 paper/make_tables.py        needs benchmarks/analysis.json (run benchmarks/analysis.py first); writes paper/numbers.tex, tab_*.tex
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__)); B = os.path.join(os.path.dirname(HERE), "benchmarks")
A = json.load(open(f"{B}/analysis.json")); Q = json.load(open(f"{B}/questions.json")); M = json.load(open(f"{B}/models.json"))
NAMES = {"ornith-9b-mtp": "Ornith 1.5 9B (MTP)", "mimo-9b": "MiMo-V2.6-Distill-Qwen 9B", "nemotron-3-nano-4b": "Nemotron 3 Nano 4B",
         "qwen2.5-coder-3b": "Qwen2.5-Coder 3B", "qwen2.5-coder-7b": "Qwen2.5-Coder 7B"}
SHORT = {"ornith-9b-mtp": "Ornith 9B", "mimo-9b": "MiMo 9B", "nemotron-3-nano-4b": "Nemotron 4B", "qwen2.5-coder-3b": "Qwen 3B", "qwen2.5-coder-7b": "Qwen 7B"}
ORDER = [m for m in NAMES if m in A["models"]]

def tex(s): return re.sub(r"([_#%&$])", r"\\\1", str(s))
def pct(x, nd=1): return f"{100 * x:.{nd}f}"
def w(name, text): open(f"{HERE}/{name}", "w").write(text)

# ---- macros
cats = {}
for q in Q: cats[q["category"]] = cats.get(q["category"], 0) + 1
mac = {"nq": A["n_questions"], "nseeds": len(A["seeds"]), "seedlist": f"{A['seeds'][0]}--{A['seeds'][-1]}", "ncells": A["cells_per_model"],
       "nregex": cats.get("regex", 0), "npython": cats.get("python", 0), "nkubectl": cats.get("kubectl", 0), "nsql": cats.get("sql", 0), "nshell": cats.get("shell", 0),
       "nnew": 29, "nboot": "10\\,000", "nmodels": len(A["models"])}
w("numbers.tex", "".join(f"\\newcommand{{\\{k}}}{{{v}}}\n" for k, v in mac.items()))

# ---- model table (from GGUF metadata read with a tiny parser)
sys.path.insert(0, B)
import struct
def gguf_arch(path):
    f = open(os.path.expanduser(path), "rb"); f.read(4); ver, nt, nkv = struct.unpack("<IQQ", f.read(20)); kv = {}
    T = {0: "<B", 1: "<b", 2: "<H", 3: "<h", 4: "<I", 5: "<i", 6: "<f", 7: "<?", 10: "<Q", 11: "<q", 12: "<d"}
    def rd(t):
        if t in T: return struct.unpack(T[t], f.read(struct.calcsize(T[t])))[0]
        if t == 8: n = struct.unpack("<Q", f.read(8))[0]; return f.read(n).decode("utf8", "replace")
        et, n = struct.unpack("<IQ", f.read(12)); [rd(et) for _ in range(n)]; return None
    for _ in range(nkv):
        n = struct.unpack("<Q", f.read(8))[0]; k = f.read(n).decode(); t = struct.unpack("<I", f.read(4))[0]; v = rd(t)
        if k in ("general.architecture",) or k.endswith(".context_length"): kv[k] = v
    return kv
src = {"ornith-9b-mtp": "protoLabsAI", "mimo-9b": "bartowski", "nemotron-3-nano-4b": "lmstudio-community", "qwen2.5-coder-3b": "lmstudio-community", "qwen2.5-coder-7b": "lmstudio-community"}
rows = []
for m in ORDER:
    spec = M[m]; p = os.path.expanduser(spec["path"]); kv = gguf_arch(p); arch = kv["general.architecture"]
    v = spec["sampling"]["vendor"]; extra = f", rep.\\ {v['repeat_penalty']}" if v.get("repeat_penalty", 1.0) != 1.0 else ""
    topk = "off" if v["top_k"] == 0 else v["top_k"]
    rows.append(f"{tex(NAMES[m])} & {tex(src[m])} & \\code{{{tex(arch)}}} & {os.path.getsize(p) / 1e9:.2f} & {kv.get(arch + '.context_length', 0) // 1024}k & "
                f"{v['temperature']} / {v['top_p']} / {topk}{extra} \\\\")
w("tab_models.tex", "\\begin{tabular}{llllrl}\\toprule Model & GGUF source & Architecture & GB & Train ctx. & Vendor sampling ($T$ / top-$p$ / top-$k$)\\\\\\midrule\n" + "\n".join(rows) + "\n\\bottomrule\\end{tabular}\n")

# ---- accuracy table (N, H, R with CIs)
sc = A["scores"]
def cell(m, c):
    r = sc[m].get(c)
    return f"{pct(r['mean'])} [{pct(r['lo'])}, {pct(r['hi'])}]" if r else "--"
rows = [f"{tex(NAMES[m])} & {cell(m, 'N')} & {cell(m, 'H')} & {cell(m, 'R')} \\\\" for m in sorted(ORDER, key=lambda m: -sc[m]["N"]["mean"])]
w("tab_scores.tex", "\\begin{tabular}{lccc}\\toprule Model & N: first attempt & H: retry with feedback & R: retry, no feedback\\\\\\midrule\n" + "\n".join(rows) + "\n\\bottomrule\\end{tabular}\n")

# ---- by category
cs = sorted(A["by_category"][ORDER[0]])
rows = [f"{tex(NAMES[m])} & " + " & ".join(f"{pct(A['by_category'][m][c]['mean'], 0)} / {pct(A['by_category'][m][c]['H'], 0)}" for c in cs) + " \\\\" for m in ORDER]
w("tab_category.tex", "\\begin{tabular}{l" + "c" * len(cs) + "}\\toprule Model & " + " & ".join(f"{c} ({cats[c]})" for c in cs) + "\\\\\\midrule\n" + "\n".join(rows) + "\n\\bottomrule\\end{tabular}\n")

# ---- pairwise
rows = [f"{tex(SHORT[p['A']])} -- {tex(SHORT[p['B']])} & {100 * p['diff']:+.1f} & [{100 * p['lo']:+.1f}, {100 * p['hi']:+.1f}] & {p['p']:.3f} & {p['p_holm']:.3f} \\\\" for p in A["pairwise"]]
w("tab_pairwise.tex", "\\begin{tabular}{lrrrr}\\toprule A -- B & $\\Delta$ (pp) & 95\\% CI & $p$ & Holm $p$\\\\\\midrule\n" + "\n".join(rows) + "\n\\bottomrule\\end{tabular}\n")

# ---- rank stability
rows = [f"{tex(NAMES[m])} & {pct(A['rank'][m]['best'], 0)}\\% & {pct(A['rank'][m]['worst'], 0)}\\% & {A['rank'][m]['mean_rank']:.2f} \\\\" for m in sorted(ORDER, key=lambda m: A["rank"][m]["mean_rank"])]
w("tab_rank.tex", "\\begin{tabular}{lrrr}\\toprule Model & P(best) & P(worst) & mean rank\\\\\\midrule\n" + "\n".join(rows) + "\n\\bottomrule\\end{tabular}\n")

# ---- effects of harness and feedback
def ef(m, k):
    e = A["effects"][m].get(k)
    return f"{100 * e['diff']:+.1f} [{100 * e['lo']:+.1f}, {100 * e['hi']:+.1f}]" if e else "--"
rows = [f"{tex(NAMES[m])} & {ef(m, 'HN')} & {ef(m, 'RN')} & {ef(m, 'HR')} \\\\" for m in ORDER]
pe = A["pooled_effects"]
if pe:
    rows.append("\\midrule All models (pooled) & " + " & ".join(f"{100 * pe[k]['diff']:+.1f} [{100 * pe[k]['lo']:+.1f}, {100 * pe[k]['hi']:+.1f}]" if k in pe else "--" for k in ("HN", "RN", "HR")) + " \\\\")
w("tab_effects.tex", "\\begin{tabular}{lccc}\\toprule Model & H $-$ N & R $-$ N & H $-$ R (feedback)\\\\\\midrule\n" + "\n".join(rows) + "\n\\bottomrule\\end{tabular}\n")

# ---- fixes (cell level)
fx = A["fixes"]
rows = [f"{tex(NAMES[m])} & {fx[m]['failed_first']} & {fx[m]['fixed_H']} & {fx[m]['fixed_R']} & {fx[m]['H_only']} & {fx[m]['R_only']} & {fx[m]['p']:.3f} \\\\" for m in ORDER if m in fx]
if "all" in fx: rows.append(f"\\midrule All & {fx['all']['failed_first']} & {fx['all']['fixed_H']} & {fx['all']['fixed_R']} & {fx['all']['H_only']} & {fx['all']['R_only']} & {fx['all']['p']:.3f} \\\\")
w("tab_fixes.tex", "\\begin{tabular}{lrrrrrr}\\toprule Model & failed first & fixed H & fixed R & H only & R only & McNemar $p$\\\\\\midrule\n" + "\n".join(rows) + "\n\\bottomrule\\end{tabular}\n")

# ---- verifier
rows = []
for c, v in A["verifier"].items():
    fa = f"{v['fp']}/{v['fp'] + v['tn']} ({pct(v['fp'] / max(1, v['fp'] + v['tn']), 0)}\\%)"; fr = f"{v['fn']}/{v['tp'] + v['fn']} ({pct(v['fn'] / max(1, v['tp'] + v['fn']), 0)}\\%)"
    rows.append(("\\midrule " if c == "all" else "") + f"{tex(c)} & {v['n']} & {pct((v['tp'] + v['fn']) / v['n'], 0)}\\% & {fa} & {fr} \\\\")
w("tab_verifier.tex", "\\begin{tabular}{lrrrr}\\toprule Task type & first attempts & hidden pass & false accept & false reject\\\\\\midrule\n" + "\n".join(rows) + "\n\\bottomrule\\end{tabular}\n")

# ---- variance and cost
rows = [f"{tex(NAMES[m])} & {A['variance'][m]['between']:.3f} & {A['variance'][m]['within']:.3f} & {A['variance'][m]['flaky']} & {A['variance'][m]['always']} & {A['variance'][m]['never']} \\\\" for m in ORDER]
w("tab_variance.tex", "\\begin{tabular}{lrrrrr}\\toprule Model & between-question var. & within-question var. & flaky & always pass & never pass\\\\\\midrule\n" + "\n".join(rows) + "\n\\bottomrule\\end{tabular}\n")
rows = [f"{tex(NAMES[m])} & {A['cost'][m]['tokens']:.0f} & {A['cost'][m]['tps']:.1f} & {A['cost'][m]['retries_per_100']:.0f} & $\\times${A['cost'][m]['time_cost_H']:.2f} \\\\" for m in ORDER]
w("tab_cost.tex", "\\begin{tabular}{lrrrr}\\toprule Model & tokens / first attempt & tok/s (first attempts) & retries per 100 cells & time cost of H\\\\\\midrule\n" + "\n".join(rows) + "\n\\bottomrule\\end{tabular}\n")

# ---- appendix: task list and per-question pass rates
def first_sentence(q):
    t = q["prompt"].split(" Reply with ONLY")[0]
    return t if len(t) < 190 else t[:187] + "..."
rows = [f"\\code{{{tex(q['id'])}}} & {q['category']} & {tex(first_sentence(q))} \\\\" for q in Q]
w("tab_tasklist.tex", "\\begin{longtable}{lll}\\toprule id & type & task (prompt, abridged)\\\\\\midrule\\endhead\n" + "\n".join(rows) + "\n\\bottomrule\\end{longtable}\n")
pq = {}
try:
    import glob
    for pth in glob.glob(f"{B}/runs/harness/*/seed*/*.json"):
        m = json.load(open(pth)); pq.setdefault((m["model"], m["question"]), []).append(m)
except Exception: pass
rows = []
for q in Q:
    cells = []
    for m in ORDER:
        ms = [c for c in pq.get((m, q["id"]), []) if c["seed"] in A["seeds"]]
        cells.append(f"{sum(c['first_pass'] for c in ms)}/{sum(c['final_pass'] for c in ms)}" if ms else "--")
    rows.append(f"\\code{{{tex(q['id'])}}} & " + " & ".join(cells) + " \\\\")
w("tab_perquestion.tex", "\\begin{longtable}{l" + "c" * len(ORDER) + "}\\toprule Task & " + " & ".join(SHORT[m] for m in ORDER) + "\\\\\\midrule\\endhead\n" + "\n".join(rows) + "\n\\bottomrule\\end{longtable}\n")
print("tables written:", sorted(f for f in os.listdir(HERE) if f.startswith("tab_") or f == "numbers.tex"))

# ---- sampling sensitivity (3 seeds, 11 original tasks): parsed from the COMPARE.md files written by repeat.py --compare
def parse_compare(path):
    rows = []
    for l in open(path):
        if l.startswith("| ") and "->" in l and "Sampling used" not in l and not l.startswith("| Question"):
            c = [x.strip() for x in l.strip().strip("|").split("|")]
            if len(c) >= 7: rows.append(c)
    return rows
out = []
for tag, lab in (("runs-vendor", "vendor"), ("runs-vendor-alt", "vendor-alt")):
    pth = f"{B}/{tag}/COMPARE.md"
    if not os.path.exists(pth): continue
    for c in parse_compare(pth):
        m = c[0]; cl = lambda x: tex(x.split(" (")[0]).replace("±", "$\\pm$")
        if m not in NAMES: continue
        out.append(f"{tex(SHORT[m])}{' (alt.\\ temp.\\ 1.0)' if lab == 'vendor-alt' else ''} & {cl(c[2])} & {cl(c[3])} & {cl(c[4])} & {cl(c[5])} \\\\")
w("tab_sampling.tex", "\\begin{tabular}{lcccc}\\toprule Model & N, ours & N, vendor & H, ours & H, vendor\\\\\\midrule\n" + "\n".join(out) + "\n\\bottomrule\\end{tabular}\n")
