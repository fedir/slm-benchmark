# Repeated-run statistics

- harness / mimo-9b: started 2026-10-17 06:32:46, uptime 542 min, 10714 MB available, swap used 696 MB, load 3.64
- harness / nemotron-3-nano-4b: started 2026-10-17 06:24:24, uptime 534 min, 10114 MB available, swap used 4 MB, load 2.6
- harness / qwen2.5-coder-3b: started 2026-10-17 06:17:51, uptime 527 min, 10016 MB available, swap used 4 MB, load 0.54
- harness / qwen2.5-coder-7b: started 2026-10-17 07:17:42, uptime 587 min, 12672 MB available, swap used 1351 MB, load 3.38

## A. Stability, no harness (first attempt, one run per seed)

| Model (source) | Seeds | Score per seed | Mean ± SD | Range | Always pass | Never pass | Flaky | Best-of-runs | Speed t/s (mean ± SD of runs) |
|---|---:|---|---|---|---:|---:|---:|---:|---|
| mimo-9b (harness first attempt) | 3 | 8/11 / 6/11 / 7/11 | 7.0 ± 1.0 | 6-8 | 5 | 2 | 4 | 9/11 | 2.8 ± 0.2 |
| nemotron-3-nano-4b (harness first attempt) | 3 | 8/11 / 8/11 / 8/11 | 8.0 ± 0.0 | 8-8 | 8 | 3 | 0 | 8/11 | 5.0 ± 0.3 |
| qwen2.5-coder-3b (harness first attempt) | 3 | 8/11 / 9/11 / 7/11 | 8.0 ± 1.0 | 7-9 | 5 | 0 | 6 | 11/11 | 8.2 ± 0.3 |
| qwen2.5-coder-7b (harness first attempt) | 3 | 8/11 / 8/11 / 9/11 | 8.3 ± 0.6 | 8-9 | 8 | 2 | 1 | 9/11 | 3.6 ± 0.0 |

Per category (mean pass count over seeds, out of the category size):

| Model | kubectl (4) | python (4) | regex (3) |
|---|---:|---:|---:|
| mimo-9b | 3.0 ± 0.0 | 2.3 ± 0.6 | 1.7 ± 0.6 |
| nemotron-3-nano-4b | 2.0 ± 0.0 | 4.0 ± 0.0 | 2.0 ± 0.0 |
| qwen2.5-coder-3b | 3.7 ± 0.6 | 3.0 ± 1.0 | 1.3 ± 1.5 |
| qwen2.5-coder-7b | 4.0 ± 0.0 | 2.3 ± 0.6 | 2.0 ± 0.0 |

### Per question: passes / runs (`*` = flaky, i.e. the model gave different outcomes across seeds)

| Question | mimo-9b | nemotron-3-nano-4b | qwen2.5-coder-3b | qwen2.5-coder-7b |
|---|---|---|---|---|
| regex-ipv4 | 1/3* | 3/3 | 2/3* | 3/3 |
| regex-date | 2/3* | 0/3 | 1/3* | 0/3 |
| regex-hexcolor | 2/3* | 3/3 | 1/3* | 3/3 |
| py-intervals | 3/3 | 3/3 | 3/3 | 3/3 |
| py-lis | 0/3 | 3/3 | 2/3* | 1/3* |
| py-topk | 1/3* | 3/3 | 1/3* | 0/3 |
| py-coins | 3/3 | 3/3 | 3/3 | 3/3 |
| kubectl-pods-sorted | 0/3 | 0/3 | 3/3 | 3/3 |
| kubectl-scale | 3/3 | 3/3 | 3/3 | 3/3 |
| kubectl-logs | 3/3 | 0/3 | 2/3* | 3/3 |
| kubectl-nodes-names | 3/3 | 3/3 | 3/3 | 3/3 |

## B. Harness: generate -> verify (public examples / offline kubectl parser) -> retry with feedback

Score = hidden-test passes out of 11, per seed, then mean ± SD over seeds.

| Model | No harness | +1 retry | +2 retries | Answers rejected by verifier per run | Fixed by retry | Broken by retry | Verifier OK but hidden test failed | Time cost |
|---|---|---|---|---|---:|---:|---:|---|
| mimo-9b | 7.0 ± 1.0 (8 / 6 / 7) | 8.7 ± 0.6 (8 / 9 / 9) | 9.3 ± 1.2 (8 / 10 / 10) | 4.0 ± 1.0 | 7 | 0 | 0 | x2.14 |
| nemotron-3-nano-4b | 8.0 ± 0.0 (8 / 8 / 8) | 8.7 ± 0.6 (9 / 9 / 8) | 8.7 ± 0.6 (9 / 9 / 8) | 3.0 ± 0.0 | 2 | 0 | 0 | x1.50 |
| qwen2.5-coder-3b | 8.0 ± 1.0 (8 / 9 / 7) | 8.7 ± 1.2 (8 / 10 / 8) | 9.0 ± 1.7 (8 / 11 / 8) | 3.0 ± 1.0 | 3 | 0 | 0 | x1.50 |
| qwen2.5-coder-7b | 8.3 ± 0.6 (8 / 8 / 9) | 10.0 ± 0.0 (10 / 10 / 10) | 10.0 ± 0.0 (10 / 10 / 10) | 2.7 ± 0.6 | 5 | 0 | 0 | x1.57 |

### Per question: passes without harness -> +1 retry -> +2 retries (over the same seeds)

| Question | mimo-9b | nemotron-3-nano-4b | qwen2.5-coder-3b | qwen2.5-coder-7b |
|---|---|---|---|---|
| regex-ipv4 | 1/3 -> 1/3 -> 1/3 | 3/3 -> 3/3 -> 3/3 | 2/3 -> 2/3 -> 2/3 | 3/3 -> 3/3 -> 3/3 |
| regex-date | 2/3 -> 2/3 -> 2/3 | 0/3 -> 1/3 -> 1/3 | 1/3 -> 1/3 -> 1/3 | 0/3 -> 3/3 -> 3/3 |
| regex-hexcolor | 2/3 -> 3/3 -> 3/3 | 3/3 -> 3/3 -> 3/3 | 1/3 -> 1/3 -> 1/3 | 3/3 -> 3/3 -> 3/3 |
| py-intervals | 3/3 -> 3/3 -> 3/3 | 3/3 -> 3/3 -> 3/3 | 3/3 -> 3/3 -> 3/3 | 3/3 -> 3/3 -> 3/3 |
| py-lis | 0/3 -> 1/3 -> 2/3 | 3/3 -> 3/3 -> 3/3 | 2/3 -> 3/3 -> 3/3 | 1/3 -> 3/3 -> 3/3 |
| py-topk | 1/3 -> 2/3 -> 3/3 | 3/3 -> 3/3 -> 3/3 | 1/3 -> 1/3 -> 2/3 | 0/3 -> 0/3 -> 0/3 |
| py-coins | 3/3 -> 3/3 -> 3/3 | 3/3 -> 3/3 -> 3/3 | 3/3 -> 3/3 -> 3/3 | 3/3 -> 3/3 -> 3/3 |
| kubectl-pods-sorted | 0/3 -> 2/3 -> 2/3 | 0/3 -> 1/3 -> 1/3 | 3/3 -> 3/3 -> 3/3 | 3/3 -> 3/3 -> 3/3 |
| kubectl-scale | 3/3 -> 3/3 -> 3/3 | 3/3 -> 3/3 -> 3/3 | 3/3 -> 3/3 -> 3/3 | 3/3 -> 3/3 -> 3/3 |
| kubectl-logs | 3/3 -> 3/3 -> 3/3 | 0/3 -> 0/3 -> 0/3 | 2/3 -> 3/3 -> 3/3 | 3/3 -> 3/3 -> 3/3 |
| kubectl-nodes-names | 3/3 -> 3/3 -> 3/3 | 3/3 -> 3/3 -> 3/3 | 3/3 -> 3/3 -> 3/3 | 3/3 -> 3/3 -> 3/3 |

## C. Retry behaviour

| Model | Retries issued | Retry returned the same code block unchanged | Retries that passed the hidden tests | Mean tokens: first attempt / retry | Attempts that hit the token cap | Longest attempt (tokens) |
|---|---:|---:|---:|---|---:|---:|
| mimo-9b | 19 | 5 | 7 | 57 / 94 | 0 | 435 |
| nemotron-3-nano-4b | 16 | 10 | 2 | 52 / 33 | 0 | 114 |
| qwen2.5-coder-3b | 16 | 4 | 3 | 73 / 56 | 0 | 224 |
| qwen2.5-coder-7b | 11 | 5 | 5 | 53 / 83 | 0 | 199 |

## D. Reproducibility of section 5 (seed 42 here vs the single run in REPORT.md section 5)

| Model | Same pass/fail outcome | Differing questions |
|---|---:|---|
| mimo-9b | 10/11 | regex-ipv4 (pass -> fail) |
| nemotron-3-nano-4b | 11/11 | none |
| qwen2.5-coder-3b | 10/11 | py-lis (fail -> pass) |
