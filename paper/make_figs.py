#!/usr/bin/env python3
"""Generate the paper's figures (matplotlib; run inside the tools container: distrobox-enter -n tools -- python3 paper/make_figs.py)."""
import json, os
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__)); B = os.path.join(os.path.dirname(HERE), "benchmarks")
A = json.load(open(f"{B}/analysis.json")); Q = json.load(open(f"{B}/questions.json"))
SHORT = {"ornith-9b-mtp": "Ornith 9B", "mimo-9b": "MiMo 9B", "nemotron-3-nano-4b": "Nemotron 4B", "qwen2.5-coder-3b": "Qwen 3B", "qwen2.5-coder-7b": "Qwen 7B"}
COL = {"N": "#233a7b", "H": "#e4006e", "R": "#7a7a7a"}
plt.rcParams.update({"font.size": 9, "axes.spines.top": False, "axes.spines.right": False, "pdf.fonttype": 42})
models = sorted(A["models"], key=lambda m: -A["scores"][m]["N"]["mean"])

# 1. forest plot of pass rate per model and condition, with question-bootstrap CIs
fig, ax = plt.subplots(figsize=(6.4, 3.0))
for i, m in enumerate(models):
    for j, (c, lab) in enumerate((("N", "first attempt"), ("H", "+2 retries, feedback"), ("R", "+2 retries, no feedback"))):
        r = A["scores"][m].get(c)
        if not r: continue
        y = i + (j - 1) * 0.24
        ax.errorbar(100 * r["mean"], y, xerr=[[100 * (r["mean"] - r["lo"])], [100 * (r["hi"] - r["mean"])]], fmt="o", color=COL[c], ms=4, capsize=2, lw=1, label=lab if i == 0 else None)
ax.set_yticks(range(len(models))); ax.set_yticklabels([SHORT[m] for m in models]); ax.invert_yaxis()
ax.set_xlabel("pass rate over questions and seeds (%), 95% bootstrap CI over questions"); ax.legend(frameon=False, fontsize=8, loc="lower left"); ax.set_xlim(0, 105)
fig.tight_layout(); fig.savefig(f"{HERE}/figs/fig_scores.pdf"); plt.close(fig)

# 2. paired effects of the harness and of feedback
fig, ax = plt.subplots(figsize=(6.4, 3.0))
for i, m in enumerate(models):
    for j, (k, lab) in enumerate((("HN", "H $-$ N (verify + retry with feedback)"), ("RN", "R $-$ N (verify + resample, no feedback)"), ("HR", "H $-$ R (what feedback adds)"))):
        e = A["effects"][m].get(k)
        if not e: continue
        ax.errorbar(100 * e["diff"], i + (j - 1) * 0.24, xerr=[[100 * (e["diff"] - e["lo"])], [100 * (e["hi"] - e["diff"])]], fmt="o", color=[COL["H"], COL["R"], COL["N"]][j], ms=4, capsize=2, lw=1, label=lab if i == 0 else None)
ax.axvline(0, color="k", lw=0.6); ax.set_yticks(range(len(models))); ax.set_yticklabels([SHORT[m] for m in models]); ax.invert_yaxis()
ax.set_xlabel("difference in pass rate (percentage points), paired by question, 95% CI"); ax.legend(frameon=False, fontsize=7.5, loc="lower right")
fig.tight_layout(); fig.savefig(f"{HERE}/figs/fig_effects.pdf"); plt.close(fig)

# 3. speed versus quality
fig, ax = plt.subplots(figsize=(4.6, 3.2))
for m in models:
    x = A["cost"][m]["tps"]
    ax.errorbar(x, 100 * A["scores"][m]["N"]["mean"], yerr=[[100 * (A["scores"][m]["N"]["mean"] - A["scores"][m]["N"]["lo"])], [100 * (A["scores"][m]["N"]["hi"] - A["scores"][m]["N"]["mean"])]], fmt="o", color=COL["N"], capsize=2, ms=5)
    ax.plot(x, 100 * A["scores"][m]["H"]["mean"], "s", color=COL["H"], ms=5)
    ax.annotate(SHORT[m], (x, 100 * A["scores"][m]["H"]["mean"]), textcoords="offset points", xytext=(5, 4), fontsize=8)
ax.plot([], [], "o", color=COL["N"], label="first attempt"); ax.plot([], [], "s", color=COL["H"], label="+2 retries with feedback")
ax.set_xlabel("generation speed on first attempts (tokens/s)"); ax.set_ylabel("pass rate (%)"); ax.legend(frameon=False, fontsize=8, loc="lower right")
fig.tight_layout(); fig.savefig(f"{HERE}/figs/fig_pareto.pdf"); plt.close(fig)

# 4. per-question pass-rate heatmap (first attempt)
import glob
cells = {}
for p in glob.glob(f"{B}/runs/harness/*/seed*/*.json"):
    m = json.load(open(p))
    if m["seed"] in A["seeds"]: cells.setdefault((m["model"], m["question"]), []).append(m["first_pass"])
qs = [q["id"] for q in Q if all((m, q["id"]) in cells for m in models)]
fig, ax = plt.subplots(figsize=(4.2, 0.2 * len(qs) + 1.0))
data = [[sum(cells[(m, q)]) / len(cells[(m, q)]) for m in models] for q in qs]
im = ax.imshow(data, cmap="Blues", vmin=0, vmax=1, aspect="auto")
ax.set_xticks(range(len(models))); ax.set_xticklabels([SHORT[m] for m in models], rotation=30, ha="right"); ax.set_yticks(range(len(qs))); ax.set_yticklabels(qs, fontsize=6.5)
fig.colorbar(im, ax=ax, fraction=0.04, pad=0.02, label="pass rate over seeds"); fig.tight_layout(); fig.savefig(f"{HERE}/figs/fig_heatmap.pdf"); plt.close(fig)

# 5. throughput (if speed.py has been run)
sp = f"{B}/speed/speed.json"
if os.path.exists(sp):
    import statistics as st
    R = [r for r in json.load(open(sp)) if "runs" in r]
    sel = [r for r in R if r["name"].endswith("/cpu-t4") or r["name"].endswith("mtp-draft2") or r["name"].endswith("vulkan-all-layers")]
    fig, ax = plt.subplots(figsize=(6.4, 3.2))
    names = [r["name"] for r in sel]; g = [[x["gen_tps"] for x in r["runs"]] for r in sel]
    ax.bar(range(len(sel)), [st.mean(x) for x in g], yerr=[st.stdev(x) for x in g], color=["#e4006e" if "vulkan" in n else "#233a7b" for n in names], capsize=2)
    ax.set_xticks(range(len(sel))); ax.set_xticklabels([n.replace("/", "\n") for n in names], rotation=60, ha="right", fontsize=6.5); ax.set_ylabel("generation (tokens/s)")
    fig.tight_layout(); fig.savefig(f"{HERE}/figs/fig_throughput.pdf"); plt.close(fig)
print("figures written")
