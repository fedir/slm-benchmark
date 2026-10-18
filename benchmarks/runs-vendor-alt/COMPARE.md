# Sampling comparison: default benchmark settings vs profile `vendor-alt`

Both sides: harness mode (first attempt = no harness, final after two retries), seeds 42/43/44, same verifier. Score = hidden-test passes out of 11.

| Model | Sampling used (default -> profile) | No harness: default | No harness: profile | +2 retries: default | +2 retries: profile | Speed t/s default -> profile |
|---|---|---|---|---|---|---|
| nemotron-3-nano-4b | T0.6 top_p0.95 top_k20 min_p0.05* rep1.0 -> T1.0 top_p0.95 top_k0 min_p0.0 rep1.0 | 8.0 ± 0.0 (8 / 8 / 8) | 6.7 ± 0.6 (6 / 7 / 7) | 8.7 ± 0.6 (9 / 9 / 8) | 8.3 ± 1.2 (7 / 9 / 9) | 5.2 -> 4.7 |

`*` = llama-server's built-in default `min_p` 0.05, which the benchmark never overrode (see REPORT.md 6.10).

## Per question: passes out of 3 seeds, default -> profile (no harness; in brackets after 2 retries)

| Question | nemotron-3-nano-4b |
|---|---|
| regex-ipv4 | 3 -> 2 (retries: 3 -> 2) **changed** |
| regex-date | 0 -> 0 (retries: 1 -> 0) **changed** |
| regex-hexcolor | 3 -> 0 (retries: 3 -> 2) **changed** |
| py-intervals | 3 -> 3 (retries: 3 -> 3) |
| py-lis | 3 -> 3 (retries: 3 -> 3) |
| py-topk | 3 -> 2 (retries: 3 -> 3) **changed** |
| py-coins | 3 -> 2 (retries: 3 -> 3) **changed** |
| kubectl-pods-sorted | 0 -> 1 (retries: 1 -> 2) **changed** |
| kubectl-scale | 3 -> 3 (retries: 3 -> 3) |
| kubectl-logs | 0 -> 1 (retries: 0 -> 1) **changed** |
| kubectl-nodes-names | 3 -> 3 (retries: 3 -> 3) |

## Per category: mean passes per seed, no harness, default -> profile

| Model | kubectl (4) | python (4) | regex (3) |
|---|---:|---:|---:|
| nemotron-3-nano-4b | 2.0 ± 0.0 -> 2.7 ± 0.6 | 4.0 ± 0.0 -> 3.3 ± 0.6 | 2.0 ± 0.0 -> 0.7 ± 0.6 |
