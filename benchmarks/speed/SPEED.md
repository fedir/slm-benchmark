# Throughput (server timings, greedy, 128 generated tokens, cache_prompt off)

Mean ± SD over the timed repetitions (warm-up discarded). Effective bandwidth = file size x generation t/s (the whole model is read once per token; with speculative decoding it can exceed the true memory traffic per token). Draft acceptance = accepted / drafted tokens.

| Configuration | file GB | n | prefill t/s | generation t/s | effective GB/s | draft acceptance | swap MB |
|---|---|---|---|---|---|---|---|
| gemma-4-e4b/cpu-t4 | 4.98 | 5 | 42.20 ± 2.68 | 6.71 ± 0.17 | 33.4 | - | 1429 |
| gemma-4-e4b/cpu-t8 | 4.98 | 5 | 44.92 ± 0.05 | 6.73 ± 0.02 | 33.5 | - | 2194 |
| gemma-4-e4b-mtp/cpu-t4 | 4.98 | 5 | 44.38 ± 0.08 | 6.41 ± 0.02 | 31.9 | 38% | 6113 |
| gemma-4-e4b-mtp/cpu-t8 | 4.98 | 5 | 44.13 ± 0.07 | 6.05 ± 0.04 | 30.1 | 38% | 6178 |
| gemma-4-e4b/cpu-t4 | 4.98 | 5 | 45.16 ± 0.08 | 6.89 ± 0.00 | 34.3 | - | 6176 |
| gemma-4-e4b-mtp/cpu-t4 | 4.98 | 5 | 44.39 ± 0.09 | 6.37 ± 0.02 | 31.7 | 38% | 6264 |
