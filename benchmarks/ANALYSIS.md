# Analysis of the extended benchmark

40 questions x 5 seeds (42, 43, 44, 45, 46) x 5 models = 1000 cells per condition. Bootstrap resamples: 10000. Questions are the unit of analysis (see `analysis.py`).

## 1. Pass rate per model and condition

Mean pass rate over questions and seeds, % (95% CI from the question bootstrap), and the per-seed score out of 40 (mean ± SD over seeds).

| Model | N: first attempt | H: +2 retries with feedback | R: +2 retries, no feedback | N per-seed score | H per-seed score |
|---|---|---|---|---|---|
| gemma-4-e4b-terse | 82.5 [70.5, 93.0] | 97.0 [91.5, 100.0] | - | 33.0 ± 1.2 | 38.8 ± 0.4 |
| nemotron-3-nano-4b | 69.0 [56.5, 80.5] | 80.0 [69.0, 89.5] | 79.5 [68.0, 90.0] | 27.6 ± 1.8 | 32.0 ± 1.2 |
| ornith-9b-mtp | 81.5 [71.5, 90.5] | 95.5 [90.5, 99.0] | 94.0 [87.5, 99.5] | 32.6 ± 1.9 | 38.2 ± 1.3 |
| qwen2.5-coder-3b | 70.0 [58.5, 81.0] | 81.0 [71.0, 90.0] | 83.5 [73.0, 93.0] | 28.0 ± 1.9 | 32.4 ± 1.5 |
| qwen2.5-coder-7b | 78.0 [66.0, 88.5] | 87.5 [78.0, 95.5] | 87.0 [77.5, 95.0] | 31.2 ± 1.8 | 35.0 ± 0.7 |

## 2. Pass rate by task type (first attempt, %, question-bootstrap 95% CI)

| Model | kubectl (10) | python (12) | regex (8) | shell (5) | sql (5) |
|---|---|---|---|---|---|
| gemma-4-e4b-terse | 82.0 [56.0, 100.0] | 91.7 [75.0, 100.0] | 85.0 [65.0, 100.0] | 60.0 [20.0, 100.0] | 80.0 [40.0, 100.0] |
| nemotron-3-nano-4b | 56.0 [30.0, 80.0] | 86.7 [68.3, 100.0] | 57.5 [30.0, 82.5] | 48.0 [12.0, 84.0] | 92.0 [76.0, 100.0] |
| ornith-9b-mtp | 84.0 [60.0, 100.0] | 78.3 [61.7, 93.3] | 87.5 [67.5, 100.0] | 72.0 [32.0, 100.0] | 84.0 [60.0, 100.0] |
| qwen2.5-coder-3b | 76.0 [54.0, 94.0] | 78.3 [55.0, 96.7] | 60.0 [35.0, 82.5] | 36.0 [8.0, 64.0] | 88.0 [72.0, 100.0] |
| qwen2.5-coder-7b | 88.0 [68.0, 100.0] | 75.0 [50.0, 96.7] | 65.0 [35.0, 92.5] | 72.0 [44.0, 96.0] | 92.0 [76.0, 100.0] |

## 3. Pairwise model differences (first attempt), paired by question

Difference in pass rate (percentage points), 95% paired-bootstrap CI, two-sided sign-flip permutation p, and Holm-adjusted p over the 10 comparisons.

| A | B | A - B (pp) | 95% CI | p | Holm p |
|---|---|---|---|---|---|
| gemma-4-e4b-terse | nemotron-3-nano-4b | +13.5 | [-0.0, +27.0] | 0.062 | 0.493 |
| gemma-4-e4b-terse | ornith-9b-mtp | +1.0 | [-8.5, +10.5] | 0.921 | 1.000 |
| gemma-4-e4b-terse | qwen2.5-coder-3b | +12.5 | [+2.5, +22.5] | 0.025 | 0.252 |
| gemma-4-e4b-terse | qwen2.5-coder-7b | +4.5 | [-8.5, +17.0] | 0.545 | 1.000 |
| nemotron-3-nano-4b | ornith-9b-mtp | -12.5 | [-25.0, -0.5] | 0.068 | 0.493 |
| nemotron-3-nano-4b | qwen2.5-coder-3b | -1.0 | [-12.5, +10.5] | 0.934 | 1.000 |
| nemotron-3-nano-4b | qwen2.5-coder-7b | -9.0 | [-23.0, +4.5] | 0.241 | 1.000 |
| ornith-9b-mtp | qwen2.5-coder-3b | +11.5 | [+2.0, +21.5] | 0.036 | 0.321 |
| ornith-9b-mtp | qwen2.5-coder-7b | +3.5 | [-8.5, +16.0] | 0.643 | 1.000 |
| qwen2.5-coder-3b | qwen2.5-coder-7b | -8.0 | [-16.0, +0.0] | 0.078 | 0.493 |

## 4. Rank stability (first attempt)

Share of question-bootstrap resamples in which each model has the highest / lowest pass rate, and its mean rank (1 = best, ties share the mean rank).

| Model | P(best) | P(worst) | mean rank |
|---|---|---|---|
| gemma-4-e4b-terse | 49.8% | 0.3% | 1.69 |
| nemotron-3-nano-4b | 0.3% | 56.0% | 4.42 |
| ornith-9b-mtp | 33.9% | 0.2% | 1.91 |
| qwen2.5-coder-3b | 0.0% | 42.4% | 4.40 |
| qwen2.5-coder-7b | 16.0% | 1.1% | 2.58 |

## 5. Effect of the harness, and of feedback versus plain resampling

Per-question paired differences in pass rate, percentage points, 95% paired-bootstrap CI, sign-flip p (Holm-adjusted over the models in each family). H - N is the total gain of verify-and-retry; R - N is the gain from the verifier plus fresh samples only; H - R is what the feedback text adds.

| Model | H - N | R - N | H - R (feedback) |
|---|---|---|---|
| gemma-4-e4b-terse | +14.5 [+5.0, +25.0] p=0.008 (Holm 0.016) | - | - |
| nemotron-3-nano-4b | +11.0 [+5.5, +18.0] p=0.000 (Holm 0.001) | +10.5 [+5.0, +17.0] p=0.001 (Holm 0.003) | +0.5 [-6.0, +8.0] p=1.000 (Holm 1.000) |
| ornith-9b-mtp | +14.0 [+6.5, +23.0] p=0.001 (Holm 0.003) | +12.5 [+6.5, +19.5] p=0.000 (Holm 0.001) | +1.5 [-4.0, +8.0] p=0.812 (Holm 1.000) |
| qwen2.5-coder-3b | +11.0 [+5.5, +18.0] p=0.000 (Holm 0.002) | +13.5 [+8.0, +19.5] p=0.000 (Holm 0.000) | -2.5 [-9.5, +5.0] p=0.598 (Holm 1.000) |
| qwen2.5-coder-7b | +9.5 [+3.0, +17.5] p=0.008 (Holm 0.016) | +9.0 [+3.5, +15.5] p=0.004 (Holm 0.004) | +0.5 [-5.5, +8.0] p=1.000 (Holm 1.000) |

Pooled over models (per-question mean of the model differences): HN: +12.0 pp [+7.4, +17.2], p=0.000; RN: +11.4 pp [+7.7, +15.4], p=0.000; HR: +0.0 pp [-4.1, +4.8], p=1.000

## 6. Failed first attempts: fixed by feedback vs fixed by resampling

Cells whose first attempt failed the hidden test (N=0). `H only` = fixed with feedback but not in the control, `R only` = fixed by the control but not with feedback (exact McNemar test on these discordant cells; cells are clustered in questions, so treat p as indicative).

| Model | failed first | fixed by H | fixed by R | H only | R only | both | neither | McNemar p |
|---|---|---|---|---|---|---|---|---|
| nemotron-3-nano-4b | 62 | 22 | 22 | 11 | 11 | 11 | 29 | 1.000 |
| ornith-9b-mtp | 37 | 28 | 25 | 10 | 7 | 18 | 2 | 0.629 |
| qwen2.5-coder-3b | 60 | 22 | 28 | 10 | 16 | 12 | 22 | 0.327 |
| qwen2.5-coder-7b | 44 | 19 | 18 | 8 | 7 | 11 | 18 | 1.000 |
| **all** | 203 | 91 | 93 | 39 | 41 | 52 | 71 | 0.911 |

## 7. Verifier quality on first attempts

Public verifier decision vs hidden test, over all first attempts. False accept = verifier passes an answer the hidden test fails (the harness would stop on a wrong answer); false reject = verifier rejects an answer the hidden test passes (a wasted retry).

| Task type | first attempts | hidden pass | verifier pass | false accept (of hidden fails) | false reject (of hidden passes) |
|---|---|---|---|---|---|
| kubectl | 250 | 77.2% | 74.0% | 0/57 (0.0%) | 8/193 (4.1%) |
| python | 300 | 82.0% | 83.0% | 3/54 (5.6%) | 0/246 (0.0%) |
| regex | 200 | 71.0% | 71.0% | 0/58 (0.0%) | 0/142 (0.0%) |
| shell | 125 | 57.6% | 67.2% | 12/53 (22.6%) | 0/72 (0.0%) |
| sql | 125 | 87.2% | 87.2% | 0/16 (0.0%) | 0/109 (0.0%) |
| all | 1000 | 76.2% | 76.9% | 15/238 (6.3%) | 8/762 (1.0%) |

## 8. Question difficulty (first attempt)

- Passed by every model on every seed (no discrimination): 11 of 40: py-intervals, py-coins, kubectl-scale, kubectl-nodes-names, py-parens, py-twosum, kubectl-label-selector, kubectl-rollout-restart, sql-top-earners, sql-dept-stats, sql-no-orders
- Never passed by any model: 0: none
- Discriminating questions: 29

| Task type | questions | mean pass rate over models | always passed by all | never passed |
|---|---|---|---|---|
| kubectl | 10 | 77.2% | 4 | 0 |
| python | 12 | 82.0% | 4 | 0 |
| regex | 8 | 71.0% | 0 | 0 |
| shell | 5 | 57.6% | 0 | 0 |
| sql | 5 | 87.2% | 3 | 0 |

## 9. Where the variance comes from

For each model, variance of the per-cell pass indicator split into between-question variance (stable difficulty) and within-question, between-seed variance (sampling noise); and the share of questions with an outcome that changes between seeds (flaky).

| Model | between-question var | within-question var | flaky questions (N) | always pass | never pass |
|---|---|---|---|---|---|
| gemma-4-e4b-terse | 0.128 | 0.016 | 4 | 31 | 5 |
| nemotron-3-nano-4b | 0.150 | 0.064 | 12 | 21 | 7 |
| ornith-9b-mtp | 0.091 | 0.060 | 13 | 26 | 1 |
| qwen2.5-coder-3b | 0.130 | 0.080 | 16 | 18 | 6 |
| qwen2.5-coder-7b | 0.130 | 0.042 | 9 | 26 | 5 |

## 10. Cost

Mean over cells. Time cost = seconds of all attempts / seconds of first attempts (harness). Tokens per first attempt; speed = completion tokens / wall-clock s of first attempts.

| Model | tokens / first attempt | speed t/s | retries issued per 100 cells | time cost H | time cost R |
|---|---|---|---|---|---|
| gemma-4-e4b-terse | 58 | 4.7 | 21 | x1.20 | - |
| nemotron-3-nano-4b | 56 | 5.5 | 46 | x1.50 | x1.31 |
| ornith-9b-mtp | 58 | 4.2 | 28 | x1.37 | x1.24 |
| qwen2.5-coder-3b | 63 | 8.9 | 48 | x1.52 | x1.40 |
| qwen2.5-coder-7b | 50 | 3.8 | 34 | x1.40 | x1.39 |
