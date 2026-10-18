# Sampling comparison: default benchmark settings vs profile `vendor`

Both sides: harness mode (first attempt = no harness, final after two retries), seeds 42/43/44, same verifier. Score = hidden-test passes out of 11.

| Model | Sampling used (default -> profile) | No harness: default | No harness: profile | +2 retries: default | +2 retries: profile | Speed t/s default -> profile |
|---|---|---|---|---|---|---|
| mimo-9b | T0.6 top_p0.95 top_k20 min_p0.05* rep1.0 -> T0.6 top_p0.95 top_k20 min_p0.0 rep1.0 | 7.3 ± 1.5 (9 / 6 / 7) | 7.0 ± 1.0 (8 / 6 / 7) | 10.0 ± 1.0 (9 / 11 / 10) | 9.3 ± 1.2 (8 / 10 / 10) | 3.0 -> 2.8 |

| nemotron-3-nano-4b | T0.6 top_p0.95 top_k20 min_p0.05* rep1.0 -> T0.6 top_p0.95 top_k0 min_p0.0 rep1.0 | 8.0 ± 0.0 (8 / 8 / 8) | 8.0 ± 0.0 (8 / 8 / 8) | 8.7 ± 0.6 (9 / 9 / 8) | 8.7 ± 0.6 (9 / 9 / 8) | 5.2 -> 5.0 |

| qwen2.5-coder-3b | T0.6 top_p0.95 top_k20 min_p0.05* rep1.0 -> T0.7 top_p0.8 top_k20 min_p0.0 rep1.05 | 8.0 ± 1.0 (7 / 9 / 8) | 8.0 ± 1.0 (8 / 9 / 7) | 9.7 ± 0.6 (10 / 9 / 10) | 9.0 ± 1.7 (8 / 11 / 8) | 8.2 -> 8.2 |

| qwen2.5-coder-7b | T0.6 top_p0.95 top_k20 min_p0.05* rep1.0 -> T0.7 top_p0.8 top_k20 min_p0.0 rep1.1 | 8.0 ± 0.0 (8 / 8 / 8) | 8.3 ± 0.6 (8 / 8 / 9) | 10.0 ± 0.0 (10 / 10 / 10) | 10.0 ± 0.0 (10 / 10 / 10) | 3.4 -> 3.6 |

`*` = llama-server's built-in default `min_p` 0.05, which the benchmark never overrode (see REPORT.md 6.10).

## Per question: passes out of 3 seeds, default -> profile (no harness; in brackets after 2 retries)

| Question | mimo-9b | nemotron-3-nano-4b | qwen2.5-coder-3b | qwen2.5-coder-7b |
|---|---|---|---|---|
| regex-ipv4 | 2 -> 1 (retries: 2 -> 1) **changed** | 3 -> 3 (retries: 3 -> 3) | 2 -> 2 (retries: 3 -> 2) **changed** | 3 -> 3 (retries: 3 -> 3) |
| regex-date | 2 -> 2 (retries: 3 -> 2) **changed** | 0 -> 0 (retries: 1 -> 1) | 1 -> 1 (retries: 1 -> 1) | 0 -> 0 (retries: 3 -> 3) |
| regex-hexcolor | 2 -> 2 (retries: 3 -> 3) | 3 -> 3 (retries: 3 -> 3) | 2 -> 1 (retries: 3 -> 1) **changed** | 3 -> 3 (retries: 3 -> 3) |
| py-intervals | 3 -> 3 (retries: 3 -> 3) | 3 -> 3 (retries: 3 -> 3) | 3 -> 3 (retries: 3 -> 3) | 3 -> 3 (retries: 3 -> 3) |
| py-lis | 0 -> 0 (retries: 2 -> 2) | 3 -> 3 (retries: 3 -> 3) | 0 -> 2 (retries: 2 -> 3) **changed** | 0 -> 1 (retries: 3 -> 3) **changed** |
| py-topk | 1 -> 1 (retries: 3 -> 3) | 3 -> 3 (retries: 3 -> 3) | 2 -> 1 (retries: 2 -> 2) **changed** | 0 -> 0 (retries: 0 -> 0) |
| py-coins | 3 -> 3 (retries: 3 -> 3) | 3 -> 3 (retries: 3 -> 3) | 3 -> 3 (retries: 3 -> 3) | 3 -> 3 (retries: 3 -> 3) |
| kubectl-pods-sorted | 0 -> 0 (retries: 2 -> 2) | 0 -> 0 (retries: 1 -> 1) | 3 -> 3 (retries: 3 -> 3) | 3 -> 3 (retries: 3 -> 3) |
| kubectl-scale | 3 -> 3 (retries: 3 -> 3) | 3 -> 3 (retries: 3 -> 3) | 3 -> 3 (retries: 3 -> 3) | 3 -> 3 (retries: 3 -> 3) |
| kubectl-logs | 3 -> 3 (retries: 3 -> 3) | 0 -> 0 (retries: 0 -> 0) | 2 -> 2 (retries: 3 -> 3) | 3 -> 3 (retries: 3 -> 3) |
| kubectl-nodes-names | 3 -> 3 (retries: 3 -> 3) | 3 -> 3 (retries: 3 -> 3) | 3 -> 3 (retries: 3 -> 3) | 3 -> 3 (retries: 3 -> 3) |

## Per category: mean passes per seed, no harness, default -> profile

| Model | kubectl (4) | python (4) | regex (3) |
|---|---:|---:|---:|
| mimo-9b | 3.0 ± 0.0 -> 3.0 ± 0.0 | 2.3 ± 0.6 -> 2.3 ± 0.6 | 2.0 ± 1.0 -> 1.7 ± 0.6 |
| nemotron-3-nano-4b | 2.0 ± 0.0 -> 2.0 ± 0.0 | 4.0 ± 0.0 -> 4.0 ± 0.0 | 2.0 ± 0.0 -> 2.0 ± 0.0 |
| qwen2.5-coder-3b | 3.7 ± 0.6 -> 3.7 ± 0.6 | 2.7 ± 0.6 -> 3.0 ± 1.0 | 1.7 ± 1.5 -> 1.3 ± 1.5 |
| qwen2.5-coder-7b | 4.0 ± 0.0 -> 4.0 ± 0.0 | 2.0 ± 0.0 -> 2.3 ± 0.6 | 2.0 ± 0.0 -> 2.0 ± 0.0 |
