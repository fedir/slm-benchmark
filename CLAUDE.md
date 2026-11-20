# SLM project

Local benchmarking of small language models on a laptop CPU/iGPU, plus a Slidev deck that presents the results. Git repo, GPL-3.0 (`LICENSE`). `slidev/` and `theme-sample.odp` are kept locally but git-ignored.

## Layout

- `REPORT.md` — source of truth for all benchmark numbers (platform, tuning, task results). The deck's benchmark slides are copied from it (3-seed mean ± SD from 6.4, harness from 6.5); update the report first, then the slides.
- `benchmarks/` — `questions.json` (11 tasks: 3 regex, 4 Python, 4 kubectl), `models.json`, `run.py` (runs + auto-grades), `results/<model>/<question>.md|json`, `results/SUMMARY.md` (the single seed-42 run).
- `benchmarks/repeat.py`, `public.json`, `runs/` — 3-seed stability runs and the generate->verify->retry harness. Per-attempt files in `runs/<mode>/<model>/seed<N>/`, tables in `runs/STATS.md`. `public.json` holds the harness's visible examples, kept disjoint from the hidden grading cases.
- `local.conf` (git-ignored; copy `local.conf.sample`) — machine-specific `MODELS_DIR` and `BACKEND_DIR`, read by `serve.sh`, the Makefile and the Python scripts (`run.py` `expand()`); `models.json` paths use `{MODELS_DIR}/...`.
- `serve.sh` + root `Makefile` — start `llama-server` (LM Studio's bundled llama.cpp Vulkan backend) on :8080. `chat.html` is a single-file chat UI for it.
- `slidev/` — the presentation (`slides.md`, `style.css`, `global-top.vue`, `global-bottom.vue`). `slides.pdf` and `dist/` (gitignored) are build outputs.
- `benchmarks/tasks_v2.py` (29 extra tasks + validation against known-good/bad answers), `run_extended.sh` (40 tasks x seeds 42-46, harness then `--mode resample` no-feedback control), `analysis.py` (bootstrap CIs over questions, paired tests -> `ANALYSIS.md`/`analysis.json`), `speed.py` (throughput with repetitions), `gguf_info.py`.
- `paper/` — LaTeX paper "Benchmarking Small Language Models...": `main.tex`, `sections/`, `refs.bib`; every number comes from `make_tables.py`/`make_figs.py` (run via `make paper`; LaTeX and matplotlib live in the `tools` distrobox).
- `TODO.md` — deferred work (remaining ideas: more seeds and questions, hidden kubectl-logs check).
- `theme-sample.odp` — visual reference the deck theme was derived from.

## Commands

Root: `make run-ornith | run-mimo | run-nemotron` (foreground server), `make stop-all`, `make benchmark [MODELS=a,b] [QUESTIONS=..] [FORCE=1]`, `make benchmark-summary`, `make benchmark-repeat MODE=naked|harness MODELS=a,b`, `make benchmark-stats`. Extended suite: `make benchmark-extended` (hours), `make benchmark-analysis`, `make benchmark-speed` (quiet machine only), `make validate-tasks`, `make paper`. Check the kubectl verifier against saved answers with `python3 benchmarks/repeat.py --kubectl-replay`. After changing a grader, re-grade saved answers with `python3 benchmarks/repeat.py --regrade` and `python3 benchmarks/run.py --regrade` (no model needed).

Deck: driven from the root via `make dev-slides` (dev server, localhost:3030, foreground), `make build-slides` (static SPA build to `slidev/dist/`), `make export-slides` (writes `slidev/slides.pdf`) — these just `$(MAKE) -C slidev run|build|pdf`. Equivalently, run inside `slidev/` directly: `make run`, `make build`, `make pdf`. All of them pass through `distrobox-enter -n tools --` automatically (see gotchas below).

## Environment gotchas

- The host has no Node. The deck runs in the `tools` distrobox container; the slidev Makefile wraps commands with `distrobox-enter -n tools --` automatically. Playwright's Chromium runtime libs (nss, nspr, pango, ...) were installed there with `dnf` for PDF export.
- `make pdf` must keep `--per-slide`: in batch export the second Mermaid diagram silently rendered blank.
- Stop `make run`/`dev-slides` before `make pdf`/`export-slides`: a dev server left running on :3030 raced the export's own headless render and produced a page 1 that just said "Loading slide…". Check with `ss -ltnp | grep 3030` and kill it first if exporting looks broken.
- `make run`/`dev-slides` must keep `NODE_OPTIONS=--dns-result-order=ipv4first`: Node in this container resolves "localhost" to `::1` only, so the dev server used to be unreachable at `http://127.0.0.1:PORT` (connection refused) even though `localhost`/`[::1]` worked — looked like a half-rendered page if a browser or proxy went via 127.0.0.1. Confirm with `ss -ltnp | grep 3030`.
- Models live in `~/.lmstudio/models/`; free RAM (~6-8 GB) and memory bandwidth are the real limits, not the iGPU.
- Models are tested "naked" (plain chat completion, no agent harness or tools) unless the harness mode is named. Quote scores as mean +/- SD over the 3 seeds (REPORT.md 6.4), not the single section 5 run; the deck's benchmark slides now do.
- Long runs: block suspend first (`systemd-inhibit --what=sleep:idle --who=benchmark --why=run sleep 7200 &`). The laptop slept mid-batch once and one request recorded 23,880 s; run one model at a time and keep other heavy work off the machine while benchmarking.

## Deck conventions

- Theme is `default` plus custom `style.css` (magenta `#e4006e` / navy `#233a7b` palette, Raleway). Content slides automatically get the full perimeter chevron frame via a `:not(.cover-chevron):not(.divider-navy):not(.bottom-band-only)` selector — no per-slide markup needed.
- Per-slide frontmatter `class:` variants: `cover-chevron` (title), `divider-navy` (wavy section/closing slides, with `.navy-panel` for text over the waves), `bottom-band-only` (sparse slides: 40px bottom band instead of the frame).
- Reusable blocks: `.feature-card` (icon cards, use `--accent`), `.stat-tile`, `.compare-card`, `.landscape-table`. Icons come from the locally installed `carbon:` and `ph:` sets only (offline).
- Pitfalls: UnoCSS `grid="~ cols-2"` was unreliable around raw HTML tables — use an inline `style="display:grid; ..."`. Markdown tables inside an HTML `<div>` break at blank lines, so use raw `<table>` there. The frame eats ~60px of height; long slides need tighter text or a smaller Mermaid `scale`.
- `global-top.vue` (corner accent) hides on the first and last page only (the Outlook slide was replaced by Conclusion), and `global-bottom.vue` (page-number pill) hides only on page 1. The divider slide at page 10 still shows the corner accent, so revisit `global-top.vue` if you add or move divider slides.
- The benchmark scripts start their own `llama-server` on port 8089 (`run.py` PORT); the chat server uses 8080. Never run `speed.py` or another benchmark while `run_extended.sh` is running (same port, and it would perturb timings).
- Sizes: report decimal GB read from the GGUF file (Ornith 5.78, MiMo 5.84, Nemotron 2.84, Qwen 3B 1.93, Qwen 7B 4.68); `ls` shows MiB.
- Finding: the harness's gain is mostly verify-and-resample, not feedback (control arm, `--mode resample`); see REPORT.md 6.5 and the paper.
