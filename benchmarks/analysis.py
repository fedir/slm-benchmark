#!/usr/bin/env python3
"""Statistical analysis of the extended benchmark (standard library only).

  analysis.py                  writes benchmarks/ANALYSIS.md and benchmarks/analysis.json from runs/{harness,resample}/
  analysis.py --boot 20000     bootstrap resamples (default 10000)

Unit of analysis. The 40 questions are the sample (Miller 2024, "Adding error bars to evals"): the seed only adds sampling noise
within a question. For each model and question the pass rate over seeds p_q is computed; a model's score is the mean of p_q over
questions. Uncertainty comes from a bootstrap over QUESTIONS (resampling questions with replacement), which also covers the
seed noise because p_q is already an average. Comparisons are paired by question (same questions for every model/condition):
paired bootstrap CI of the mean difference and a sign-flip permutation test on the per-question differences, Holm-adjusted
within each family of comparisons. Conditions per cell: N = first attempt (no harness), H = after <=2 retries with feedback,
R = after <=2 retries with NO feedback (fresh sample, new seed; control arm). All three share the same first attempt.
"""
import argparse, glob, itertools, json, math, os, random, statistics as st

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS = os.path.join(HERE, "runs")
RNG = random.Random(20261017)

def load(mode):
    d = {}
    for p in glob.glob(f"{RUNS}/{mode}/*/seed*/*.json"):
        m = json.load(open(p))
        d.setdefault(m["model"], {}).setdefault(m["question"], {})[m["seed"]] = m
    return d

def mean(x): x = list(x); return sum(x) / len(x) if x else float("nan")

def boot_ci(vals, nboot, stat=mean):
    """95% percentile bootstrap CI of stat over the list `vals` (resampling items with replacement)."""
    n = len(vals); out = []
    for _ in range(nboot):
        out.append(stat([vals[RNG.randrange(n)] for _ in range(n)]))
    out.sort()
    return out[int(0.025 * nboot)], out[int(0.975 * nboot) - 1]

def sign_flip_p(diffs, nperm=100000):
    """Two-sided sign-flip permutation test on paired per-question differences (exact for <= 16 non-zero, else Monte Carlo)."""
    d = [x for x in diffs if abs(x) > 1e-12]
    if not d: return 1.0
    obs = abs(sum(d))
    if len(d) <= 16:
        cnt = sum(1 for signs in itertools.product((1, -1), repeat=len(d)) if abs(sum(s * x for s, x in zip(signs, d))) >= obs - 1e-12)
        return cnt / 2 ** len(d)
    cnt = sum(1 for _ in range(nperm) if abs(sum(x if RNG.random() < 0.5 else -x for x in d)) >= obs - 1e-12)
    return (cnt + 1) / (nperm + 1)

def holm(ps):
    order = sorted(range(len(ps)), key=lambda i: ps[i]); adj = [0.0] * len(ps); run = 0.0
    for rank, i in enumerate(order):
        run = max(run, min(1.0, (len(ps) - rank) * ps[i])); adj[i] = run
    return adj

def binom_two_sided(b, c):
    n = b + c
    if n == 0: return 1.0
    k = min(b, c)
    return min(1.0, 2 * sum(math.comb(n, i) for i in range(k + 1)) / 2 ** n)

def fmt(x, nd=2): return f"{x:.{nd}f}"
def pct(x): return f"{100 * x:.1f}"

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--boot", type=int, default=10000); ap.add_argument("--models", help="comma-separated subset (preview while a run is incomplete)"); a = ap.parse_args()
    H, R = load("harness"), load("resample")
    questions = json.load(open(f"{HERE}/questions.json")); cat = {q["id"]: q["category"] for q in questions}
    models = sorted(a.models.split(",")) if a.models else sorted(H)
    # balanced dataset: questions and seeds present for every model in harness mode
    qs = sorted(set.intersection(*[set(H[m]) for m in models]), key=lambda q: [x["id"] for x in questions].index(q))
    seeds = sorted(set.intersection(*[set(s for q in qs for s in H[m][q]) for m in models]))
    seeds = [s for s in seeds if all(all(s in H[m][q] for q in qs) for m in models)]
    hasR = {m: all(all(s in R.get(m, {}).get(q, {}) for s in seeds) for q in qs) for m in models}
    out = {"models": models, "n_questions": len(qs), "seeds": seeds, "cells_per_model": len(qs) * len(seeds)}
    md = [f"# Analysis of the extended benchmark", "",
          f"{len(qs)} questions x {len(seeds)} seeds ({', '.join(map(str, seeds))}) x {len(models)} models = "
          f"{len(qs) * len(seeds) * len(models)} cells per condition. Bootstrap resamples: {a.boot}. Questions are the unit of analysis (see `analysis.py`).", ""]

    def pq(model, q, key, src=H):
        cells = [src[model][q][s] for s in seeds]
        return mean(c[key] for c in cells)
    P = {m: {"N": {q: pq(m, q, "first_pass") for q in qs}, "H": {q: pq(m, q, "final_pass") for q in qs},
             **({"R": {q: pq(m, q, "final_pass", R) for q in qs}} if hasR[m] else {})} for m in models}

    # ---- 1. scores with CIs
    md += ["## 1. Pass rate per model and condition", "",
           "Mean pass rate over questions and seeds, % (95% CI from the question bootstrap), and the per-seed score out of "
           f"{len(qs)} (mean ± SD over seeds).", "",
           "| Model | N: first attempt | H: +2 retries with feedback | R: +2 retries, no feedback | N per-seed score | H per-seed score |", "|---|---|---|---|---|---|"]
    out["scores"] = {}
    for m in models:
        row = [m]; rec = {}
        for cond in ("N", "H", "R"):
            if cond not in P[m]: row.append("-"); continue
            v = [P[m][cond][q] for q in qs]; lo, hi = boot_ci(v, a.boot)
            rec[cond] = {"mean": mean(v), "lo": lo, "hi": hi}; row.append(f"{pct(mean(v))} [{pct(lo)}, {pct(hi)}]")
        for cond, key in (("N", "first_pass"), ("H", "final_pass")):
            per = [sum(H[m][q][s][key] for q in qs) for s in seeds]
            rec[f"{cond}_seed_scores"] = per
            row.append(f"{mean(per):.1f} ± {st.stdev(per):.1f}" if len(per) > 1 else str(per[0]))
        out["scores"][m] = rec; md.append("| " + " | ".join(row) + " |")
    md.append("")

    # ---- 2. by category
    cats = sorted(set(cat[q] for q in qs))
    md += ["## 2. Pass rate by task type (first attempt, %, question-bootstrap 95% CI)", "",
           "| Model | " + " | ".join(f"{c} ({sum(1 for q in qs if cat[q] == c)})" for c in cats) + " |", "|---|" + "---|" * len(cats)]
    out["by_category"] = {}
    for m in models:
        row = [m]; out["by_category"][m] = {}
        for c in cats:
            v = [P[m]["N"][q] for q in qs if cat[q] == c]; lo, hi = boot_ci(v, a.boot)
            out["by_category"][m][c] = {"mean": mean(v), "lo": lo, "hi": hi, "H": mean(P[m]["H"][q] for q in qs if cat[q] == c)}
            row.append(f"{pct(mean(v))} [{pct(lo)}, {pct(hi)}]")
        md.append("| " + " | ".join(row) + " |")
    md.append("")

    # ---- 3. pairwise model comparison (N)
    md += ["## 3. Pairwise model differences (first attempt), paired by question", "",
           "Difference in pass rate (percentage points), 95% paired-bootstrap CI, two-sided sign-flip permutation p, and Holm-adjusted p over the "
           f"{len(models) * (len(models) - 1) // 2} comparisons.", "", "| A | B | A - B (pp) | 95% CI | p | Holm p |", "|---|---|---|---|---|---|"]
    pairs = list(itertools.combinations(models, 2)); rows = []; ps = []
    for A, B in pairs:
        d = [P[A]["N"][q] - P[B]["N"][q] for q in qs]; lo, hi = boot_ci(d, a.boot); p = sign_flip_p(d)
        rows.append((A, B, mean(d), lo, hi, p)); ps.append(p)
    adj = holm(ps); out["pairwise"] = []
    for (A, B, dm, lo, hi, p), ap_ in zip(rows, adj):
        out["pairwise"].append({"A": A, "B": B, "diff": dm, "lo": lo, "hi": hi, "p": p, "p_holm": ap_})
        md.append(f"| {A} | {B} | {100 * dm:+.1f} | [{100 * lo:+.1f}, {100 * hi:+.1f}] | {p:.3f} | {ap_:.3f} |")
    md.append("")

    # ---- 4. rank stability
    md += ["## 4. Rank stability (first attempt)", "",
           "Share of question-bootstrap resamples in which each model has the highest / lowest pass rate, and its mean rank (1 = best, ties share the mean rank).", "",
           "| Model | P(best) | P(worst) | mean rank |", "|---|---|---|---|"]
    best = {m: 0 for m in models}; worst = {m: 0 for m in models}; rk = {m: 0.0 for m in models}; nb = a.boot
    for _ in range(nb):
        idx = [RNG.randrange(len(qs)) for _ in qs]; sc = {m: mean(P[m]["N"][qs[i]] for i in idx) for m in models}
        top, bot = max(sc.values()), min(sc.values())
        for m in models:
            best[m] += (sc[m] == top) / sum(1 for x in sc.values() if x == top); worst[m] += (sc[m] == bot) / sum(1 for x in sc.values() if x == bot)
            rk[m] += 1 + sum(1 for o in models if sc[o] > sc[m]) + 0.5 * (sum(1 for o in models if sc[o] == sc[m]) - 1)
    out["rank"] = {m: {"best": best[m] / nb, "worst": worst[m] / nb, "mean_rank": rk[m] / nb} for m in models}
    for m in models: md.append(f"| {m} | {pct(best[m] / nb)}% | {pct(worst[m] / nb)}% | {rk[m] / nb:.2f} |")
    md.append("")

    # ---- 5. harness effect and feedback effect
    md += ["## 5. Effect of the harness, and of feedback versus plain resampling", "",
           "Per-question paired differences in pass rate, percentage points, 95% paired-bootstrap CI, sign-flip p (Holm-adjusted over the models in each family). "
           "H - N is the total gain of verify-and-retry; R - N is the gain from the verifier plus fresh samples only; H - R is what the feedback text adds.", "",
           "| Model | H - N | R - N | H - R (feedback) |", "|---|---|---|---|"]
    out["effects"] = {}; fam = {"HN": [], "RN": [], "HR": []}
    for m in models:
        out["effects"][m] = {}
        for key, (x, y) in {"HN": ("H", "N"), "RN": ("R", "N"), "HR": ("H", "R")}.items():
            if x in P[m] and y in P[m]:
                d = [P[m][x][q] - P[m][y][q] for q in qs]; lo, hi = boot_ci(d, a.boot); p = sign_flip_p(d)
                out["effects"][m][key] = {"diff": mean(d), "lo": lo, "hi": hi, "p": p}; fam[key].append((m, p))
    for key in fam:
        adjp = dict(zip([m for m, _ in fam[key]], holm([p for _, p in fam[key]])))
        for m, _ in fam[key]: out["effects"][m][key]["p_holm"] = adjp[m]
    for m in models:
        cells = []
        for key in ("HN", "RN", "HR"):
            e = out["effects"][m].get(key)
            cells.append(f"{100 * e['diff']:+.1f} [{100 * e['lo']:+.1f}, {100 * e['hi']:+.1f}] p={e['p']:.3f} (Holm {e['p_holm']:.3f})" if e else "-")
        md.append(f"| {m} | " + " | ".join(cells) + " |")
    # pooled over models
    pooled = {}
    for key, (x, y) in {"HN": ("H", "N"), "RN": ("R", "N"), "HR": ("H", "R")}.items():
        ms = [m for m in models if x in P[m] and y in P[m]]
        if not ms: continue
        d = [mean(P[m][x][q] - P[m][y][q] for m in ms) for q in qs]; lo, hi = boot_ci(d, a.boot)
        pooled[key] = {"diff": mean(d), "lo": lo, "hi": hi, "p": sign_flip_p(d), "models": len(ms)}
    out["pooled_effects"] = pooled
    md += ["", "Pooled over models (per-question mean of the model differences): " + "; ".join(
        f"{k}: {100 * v['diff']:+.1f} pp [{100 * v['lo']:+.1f}, {100 * v['hi']:+.1f}], p={v['p']:.3f}" for k, v in pooled.items()), ""]

    # ---- 6. cell-level fixes (McNemar on cells that failed first)
    md += ["## 6. Failed first attempts: fixed by feedback vs fixed by resampling", "",
           "Cells whose first attempt failed the hidden test (N=0). `H only` = fixed with feedback but not in the control, `R only` = fixed by the control but not with feedback "
           "(exact McNemar test on these discordant cells; cells are clustered in questions, so treat p as indicative).", "",
           "| Model | failed first | fixed by H | fixed by R | H only | R only | both | neither | McNemar p |", "|---|---|---|---|---|---|---|---|---|"]
    out["fixes"] = {}; tot = [0] * 6
    for m in models:
        if not hasR[m]: continue
        b = c = both = nei = fh = fr = n0 = 0
        for q in qs:
            for s in seeds:
                h, r = H[m][q][s], R[m][q][s]
                if h["first_pass"]: continue
                n0 += 1; fh += h["final_pass"]; fr += r["final_pass"]
                if h["final_pass"] and r["final_pass"]: both += 1
                elif h["final_pass"]: b += 1
                elif r["final_pass"]: c += 1
                else: nei += 1
        out["fixes"][m] = {"failed_first": n0, "fixed_H": fh, "fixed_R": fr, "H_only": b, "R_only": c, "both": both, "neither": nei, "p": binom_two_sided(b, c)}
        for i, v in enumerate((n0, fh, fr, b, c, both)): tot[i] += v
        md.append(f"| {m} | {n0} | {fh} | {fr} | {b} | {c} | {both} | {nei} | {binom_two_sided(b, c):.3f} |")
    tn = sum(out["fixes"][m]["neither"] for m in out["fixes"])
    md.append(f"| **all** | {tot[0]} | {tot[1]} | {tot[2]} | {tot[3]} | {tot[4]} | {tot[5]} | {tn} | {binom_two_sided(tot[3], tot[4]):.3f} |")
    out["fixes"]["all"] = {"failed_first": tot[0], "fixed_H": tot[1], "fixed_R": tot[2], "H_only": tot[3], "R_only": tot[4], "both": tot[5], "neither": tn, "p": binom_two_sided(tot[3], tot[4])}
    md.append("")

    # ---- 7. verifier quality on first attempts
    md += ["## 7. Verifier quality on first attempts", "",
           "Public verifier decision vs hidden test, over all first attempts. False accept = verifier passes an answer the hidden test fails (the harness would stop on a wrong answer); "
           "false reject = verifier rejects an answer the hidden test passes (a wasted retry).", "",
           "| Task type | first attempts | hidden pass | verifier pass | false accept (of hidden fails) | false reject (of hidden passes) |", "|---|---|---|---|---|---|"]
    out["verifier"] = {}
    for c in cats + ["all"]:
        tp = fp = fn = tn_ = 0
        for m in models:
            for q in qs:
                if c != "all" and cat[q] != c: continue
                for s in seeds:
                    at = H[m][q][s]["attempts"][0]; hp, vp = at["hidden_pass"], at["verifier_pass"]
                    if hp and vp: tp += 1
                    elif hp and not vp: fn += 1
                    elif not hp and vp: fp += 1
                    else: tn_ += 1
        n = tp + fp + fn + tn_; out["verifier"][c] = {"n": n, "tp": tp, "fp": fp, "fn": fn, "tn": tn_}
        md.append(f"| {c} | {n} | {pct((tp + fn) / n)}% | {pct((tp + fp) / n)}% | {fp}/{fp + tn_} ({pct(fp / max(1, fp + tn_))}%) | {fn}/{tp + fn} ({pct(fn / max(1, tp + fn))}%) |")
    md.append("")

    # ---- 8. question difficulty
    qrate = {q: mean(P[m]["N"][q] for m in models) for q in qs}
    never = [q for q in qs if all(P[m]["N"][q] == 0 for m in models)]; always = [q for q in qs if all(P[m]["N"][q] == 1 for m in models)]
    split = [q for q in qs if q not in never and q not in always]
    md += ["## 8. Question difficulty (first attempt)", "",
           f"- Passed by every model on every seed (no discrimination): {len(always)} of {len(qs)}: {', '.join(always) or 'none'}",
           f"- Never passed by any model: {len(never)}: {', '.join(never) or 'none'}",
           f"- Discriminating questions: {len(split)}", "",
           "| Task type | questions | mean pass rate over models | always passed by all | never passed |", "|---|---|---|---|---|"]
    out["difficulty"] = {"always": always, "never": never, "split": len(split), "per_question": qrate}
    for c in cats:
        qq = [q for q in qs if cat[q] == c]
        md.append(f"| {c} | {len(qq)} | {pct(mean(qrate[q] for q in qq))}% | {sum(q in always for q in qq)} | {sum(q in never for q in qq)} |")
    md.append("")

    # ---- 9. variance: seed vs question
    md += ["## 9. Where the variance comes from", "",
           "For each model, variance of the per-cell pass indicator split into between-question variance (stable difficulty) and within-question, between-seed variance (sampling noise); "
           "and the share of questions with an outcome that changes between seeds (flaky).", "",
           "| Model | between-question var | within-question var | flaky questions (N) | always pass | never pass |", "|---|---|---|---|---|---|"]
    out["variance"] = {}
    for m in models:
        cellvals = [[H[m][q][s]["first_pass"] for s in seeds] for q in qs]; allv = [x for r in cellvals for x in r]; g = mean(allv)
        within = mean(mean((x - mean(r)) ** 2 for x in r) for r in cellvals); between = mean((mean(r) - g) ** 2 for r in cellvals)
        fl = sum(1 for r in cellvals if 0 < sum(r) < len(r)); al = sum(1 for r in cellvals if sum(r) == len(r)); ne = sum(1 for r in cellvals if sum(r) == 0)
        out["variance"][m] = {"between": between, "within": within, "flaky": fl, "always": al, "never": ne}
        md.append(f"| {m} | {between:.3f} | {within:.3f} | {fl} | {al} | {ne} |")
    md.append("")

    # ---- 10. cost
    md += ["## 10. Cost", "", "Mean over cells. Time cost = seconds of all attempts / seconds of first attempts (harness). Tokens per first attempt; speed = completion tokens / wall-clock s of first attempts.", "",
           "| Model | tokens / first attempt | speed t/s | retries issued per 100 cells | time cost H | time cost R |", "|---|---|---|---|---|---|"]
    out["cost"] = {}
    for m in models:
        cells = [H[m][q][s] for q in qs for s in seeds]
        tok = mean(c["attempts"][0]["tokens"] for c in cells); tps = sum(c["attempts"][0]["tokens"] for c in cells) / sum(c["attempts"][0]["seconds"] for c in cells)
        ret = 100 * sum(len(c["attempts"]) - 1 for c in cells) / len(cells)
        tc = sum(c["seconds_total"] for c in cells) / sum(c["attempts"][0]["seconds"] for c in cells)
        tr = "-"
        if hasR[m]:
            rc = [R[m][q][s] for q in qs for s in seeds]; tr = f"x{sum(c['seconds_total'] for c in rc) / sum(c['attempts'][0]['seconds'] for c in rc):.2f}"
        out["cost"][m] = {"tokens": tok, "tps": tps, "retries_per_100": ret, "time_cost_H": tc}
        md.append(f"| {m} | {tok:.0f} | {tps:.1f} | {ret:.0f} | x{tc:.2f} | {tr} |")
    md.append("")
    open(f"{HERE}/ANALYSIS.md", "w").write("\n".join(md)); json.dump(out, open(f"{HERE}/analysis.json", "w"), indent=1)
    print("\n".join(md))

if __name__ == "__main__":
    main()
