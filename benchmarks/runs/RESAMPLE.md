# Control arm: retry with feedback vs retry without feedback (fresh sample, new seed)

Same first attempts, same verifier trigger, up to 2 retries; hidden tests grade. Score /11, mean ± SD over seeds 42/43/44.

| Model | No retry | + 2 retries WITH feedback (harness) | + 2 retries WITHOUT feedback (control) | Cells fixed: feedback / no feedback | Cells broken: feedback / no feedback |
|---|---|---|---|---|---|
| gemma-4-e4b-terse | 35.0 (35) | 38.0 (38) | 35.0 (35) | 3 / 0 | 0 / 0 |
| nemotron-3-nano-4b | 27.6 ± 1.8 (30 / 27 / 28 / 25 / 28) | 32.0 ± 1.2 (32 / 33 / 32 / 30 / 33) | 31.8 ± 0.8 (33 / 31 / 32 / 32 / 31) | 22 / 22 | 0 / 1 |
| ornith-9b-mtp | 32.6 ± 1.9 (35 / 32 / 32 / 30 / 34) | 38.2 ± 1.3 (40 / 37 / 37 / 38 / 39) | 37.6 ± 0.9 (38 / 38 / 38 / 36 / 38) | 28 / 25 | 0 / 0 |
| qwen2.5-coder-3b | 28.0 ± 1.9 (28 / 30 / 29 / 28 / 25) | 32.4 ± 1.5 (31 / 32 / 35 / 32 / 32) | 33.4 ± 1.7 (32 / 34 / 32 / 36 / 33) | 22 / 28 | 0 / 1 |
| qwen2.5-coder-7b | 31.2 ± 1.8 (32 / 30 / 30 / 34 / 30) | 35.0 ± 0.7 (35 / 34 / 35 / 36 / 35) | 34.8 ± 1.3 (34 / 33 / 35 / 36 / 36) | 19 / 18 | 0 / 0 |

All models: cells fixed 94 with feedback vs 93 without; cells broken 0 vs 2.
By type (fixed with / without feedback): regex+Python 60 / 75, kubectl 34 / 18.
