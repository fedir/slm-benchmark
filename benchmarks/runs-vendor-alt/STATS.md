# Repeated-run statistics

- harness / nemotron-3-nano-4b: started 2026-10-17 06:55:40, uptime 565 min, 10088 MB available, swap used 2399 MB, load 5.78

## A. Stability, no harness (first attempt, one run per seed)

| Model (source) | Seeds | Score per seed | Mean ± SD | Range | Always pass | Never pass | Flaky | Best-of-runs | Speed t/s (mean ± SD of runs) |
|---|---:|---|---|---|---:|---:|---:|---:|---|
| nemotron-3-nano-4b (harness first attempt) | 3 | 6/11 / 7/11 / 7/11 | 6.7 ± 0.6 | 6-7 | 4 | 2 | 5 | 9/11 | 4.7 ± 0.2 |

Per category (mean pass count over seeds, out of the category size):

| Model | kubectl (4) | python (4) | regex (3) |
|---|---:|---:|---:|
| nemotron-3-nano-4b | 2.7 ± 0.6 | 3.3 ± 0.6 | 0.7 ± 0.6 |

### Per question: passes / runs (`*` = flaky, i.e. the model gave different outcomes across seeds)

| Question | nemotron-3-nano-4b |
|---|---|
| regex-ipv4 | 2/3* |
| regex-date | 0/3 |
| regex-hexcolor | 0/3 |
| py-intervals | 3/3 |
| py-lis | 3/3 |
| py-topk | 2/3* |
| py-coins | 2/3* |
| kubectl-pods-sorted | 1/3* |
| kubectl-scale | 3/3 |
| kubectl-logs | 1/3* |
| kubectl-nodes-names | 3/3 |

## B. Harness: generate -> verify (public examples / offline kubectl parser) -> retry with feedback

Score = hidden-test passes out of 11, per seed, then mean ± SD over seeds.

| Model | No harness | +1 retry | +2 retries | Answers rejected by verifier per run | Fixed by retry | Broken by retry | Verifier OK but hidden test failed | Time cost |
|---|---|---|---|---|---:|---:|---:|---|
| nemotron-3-nano-4b | 6.7 ± 0.6 (6 / 7 / 7) | 8.3 ± 1.2 (7 / 9 / 9) | 8.3 ± 1.2 (7 / 9 / 9) | 4.3 ± 0.6 | 5 | 0 | 1 | x1.68 |

### Per question: passes without harness -> +1 retry -> +2 retries (over the same seeds)

| Question | nemotron-3-nano-4b |
|---|---|
| regex-ipv4 | 2/3 -> 2/3 -> 2/3 |
| regex-date | 0/3 -> 0/3 -> 0/3 |
| regex-hexcolor | 0/3 -> 2/3 -> 2/3 |
| py-intervals | 3/3 -> 3/3 -> 3/3 |
| py-lis | 3/3 -> 3/3 -> 3/3 |
| py-topk | 2/3 -> 3/3 -> 3/3 |
| py-coins | 2/3 -> 3/3 -> 3/3 |
| kubectl-pods-sorted | 1/3 -> 2/3 -> 2/3 |
| kubectl-scale | 3/3 -> 3/3 -> 3/3 |
| kubectl-logs | 1/3 -> 1/3 -> 1/3 |
| kubectl-nodes-names | 3/3 -> 3/3 -> 3/3 |

## C. Retry behaviour

| Model | Retries issued | Retry returned the same code block unchanged | Retries that passed the hidden tests | Mean tokens: first attempt / retry | Attempts that hit the token cap | Longest attempt (tokens) |
|---|---:|---:|---:|---|---:|---:|
| nemotron-3-nano-4b | 20 | 9 | 5 | 53 / 40 | 0 | 147 |

## D. Reproducibility of section 5 (seed 42 here vs the single run in REPORT.md section 5)

| Model | Same pass/fail outcome | Differing questions |
|---|---:|---|
| nemotron-3-nano-4b | 7/11 | regex-ipv4 (pass -> fail), regex-hexcolor (pass -> fail), py-coins (pass -> fail), kubectl-pods-sorted (fail -> pass) |
