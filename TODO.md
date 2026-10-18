# TODO

Done: Slidev deck updated to the 3-seed and harness numbers (slides 11-18, 2026-10-17); generate -> verify -> retry harness and 3-seed stability runs for all four models (REPORT.md section 6,
`benchmarks/repeat.py`, `benchmarks/runs/STATS.md`).

Next:

- **Hidden `kubectl-logs` check is too strict.** It requires `-c app` but `kubectl logs POD CONTAINER` is valid; one Qwen attempt
  (seed 43) is graded a fail for that. Fixing it changes that cell to a pass (REPORT.md 6.9). The stronger kubectl verifier and its
  re-run are done.
- Harness control arm: done (REPORT.md 6.5; `--mode resample`). Follow-up: a control with a larger retry budget and on tasks no model can pass by luck.
- **More seeds (5 or more) and more questions**, to separate Nemotron, Qwen and MiMo, whose differences are inside
  the seed-to-seed spread.
- Hardware ideas not tried (REPORT.md 7.6): `performance` energy preference and cooling (the CPU runs at ~90 C),
  an AVX-512 native llama.cpp build, smaller quantisations.
- Gemma 4 E4B (terse system prompt, Gemma only): harness on 5 seeds, control arm on seed 42 only (REPORT.md 6.12, 6.13). Still to do: its 5-seed control arm, and a clean speed re-measurement (MTP vs plain).

## Remaining work (estimated, as of 2026-10-17)

Minimum path (~1-1.25 h):
- [ ] Reduced throughput test on a quiet machine (`python3 benchmarks/speed.py -c ...`: 5 models at 4 threads + Gemma with/without MTP), ~25 min; nothing else may run. Cleans the swap-confounded Gemma timings.
- [ ] `python3 paper/make_tables.py` and `distrobox-enter -n tools -- python3 paper/make_figs.py` for the 5 models (~5 min)
- [ ] Paper text: `paper/sections/abstract.tex`, `paper/sections/results.tex`, define `\resultsummary` and `\discussiontext`, then `make paper` (~30-40 min); confirm the 5 unverified references
- [ ] Re-export the slides PDF after final edits (~2 min; stop the dev server first)

Optional (machine time):
- [ ] Full throughput test, all configurations, 7 repetitions (~60-75 min)
- [ ] Gemma control arm on seeds 43-46 (~50 min); currently seed 42 only
- [ ] Rewrite the Qwen 3B 11-task rows in REPORT.md 6.4, 6.5, 6.10 and summary items (post `kubectl-logs` fix: 8.0 ± 1.0 / 9.7 ± 0.6 / control 10.3 ± 0.6)
- [ ] Slides: add a statistics page, a throughput page, and the Gemma MTP result on the MTP page (after the speed test)
