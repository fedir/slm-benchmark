# Running small language models on a laptop CPU/iGPU

Findings from setting up and benchmarking local LLMs on an Intel ultrabook, October 2026.
All numbers below were measured in this project unless marked otherwise.

## 1. Platform

| Item | Value |
|---|---|
| CPU | Intel Core i7-1165G7 @ 2.80 GHz (4 physical cores / 8 threads) |
| RAM | 15.3 GB total, shared with the GPU; ~6-8 GB free during tests |
| RAM bandwidth | ~34 GB/s (measured by the capability scan) |
| GPU | Intel Iris Xe (TigerLake-LP GT2), integrated, unified memory |
| OS | Fedora 43 (immutable, Flatpak apps) |
| Swap | 8 GB, almost full (7.8 GB used) during the Ornith/MiMo runs |
| Inference engine | `llama-server` from LM Studio's bundled llama.cpp **Vulkan** backend, v2.54.0 (no standalone llama.cpp install, no `llama-bench`) |
| Models dir | `~/.lmstudio/models/` |

**The governing constraint is memory bandwidth.** Token generation reads the whole model
once per token, so the ceiling is roughly `bandwidth / model size`. 34 GB/s is the scan's peak figure; the best measured effective bandwidth is
about 20 GB/s (Qwen 3B: 10.7 t/s on 1.9 GB), so realistic ceilings are about 3.4 t/s for a 5.8 GB model without MTP and ~10 t/s for 1.9 GB
(the 34 GB/s peak would give ~6 and ~18 t/s). The iGPU shares the same RAM
bus, so it adds no bandwidth.

### Project files

| File | Purpose |
|---|---|
| `LICENSE` | GNU General Public License v3.0 |
| `local.conf.sample` | Template for the git-ignored `local.conf` (model directory and llama.cpp backend path) |
| `serve.sh` | Starts `llama-server`; `MODEL=` and `SPEC=` env vars override the defaults |
| `Makefile` | `make run-ornith`, `make run-mimo`, `make stop-all`, `make help` |
| `chat.html` | Single-file chat UI for the server (see 2) |
| `benchmarks/` | `questions.json`, `models.json`, `run.py`, and `results/<model>/<question>.md` (see 5) |
| `benchmarks/repeat.py`, `public.json`, `runs/` | repeated seeds and the verify-retry harness; per-run files in `runs/<mode>/<model>/seed<N>/`, tables in `runs/STATS.md` (see 6) |

Default server settings: CPU only (`-ngl 0 -t 4`), 16k context, port 8080. Ornith also
runs with `--spec-type draft-mtp --spec-draft-n-max 2`.

## 2. Chat UI

`chat.html` talks to the server's OpenAI-compatible `/v1/chat/completions` endpoint with
streaming. Controls:

- **Thinking**: off, low (128 tokens), medium (512), high (2048), unlimited. Off sends
  `chat_template_kwargs.enable_thinking=false`; the levels send `thinking_budget_tokens`.
  Default: off.
- **Max output**: 128 to 4096 or no limit, sent as `max_tokens` (it counts thinking and
  answer together). Default: 512.
- **Sampling**: *general* (temp 1.0, top_p 0.95, top_k 20, min_p 0, presence_penalty 1.5)
  or *precise coding* (temp 0.6, presence_penalty 0), the two presets on the Ornith model card.
- Reasoning text is shown in a separate muted block; each reply ends with a tokens/s line.
  Settings persist in `localStorage`.

## 3. Methodology

### 3.1 Candidate selection
An early hardware-compatibility scan (6,605 entries marked "perfect" or "good" fit, 4,338 / 2,267, mostly at Q8_0; the file itself is no longer in the project) was **not trusted** for two reasons:

- it treats all 15.3 GB as available (only ~6-8 GB really is);
- its `estimated_tps` is optimistic: it predicted 28 t/s for a 3B Q8 model, against a
  bandwidth ceiling of ~8 t/s for that size.

It was used only to shortlist families; sizes were then judged against free RAM and the
bandwidth ceiling.

### 3.2 Benchmark procedure
- One `llama-server` instance per configuration, loaded from the same GGUF and quantisation
  family (Q4_K_M) where possible.
- Timings read from the server (`prompt_per_second`, `predicted_per_second`) or computed
  from `completion_tokens` / wall time on the chat endpoint.
- Speed sweep (Qwen2.5-Coder-3B): ~280-token prompt, 64-200 generated tokens, then a
  code-generation prompt for the speculative-decoding tests, whose acceptance rate depends
  on the content.
- Model comparison: 3 identical prompts (code, short explanation, arithmetic), thinking off,
  `max_tokens=200`, temperature 0.6, top_p 0.95, top_k 20 (plus llama-server's default `min_p` 0.05, which was never overridden; see 6.10).
- Device placement checked in verbose logs (`layer N assigned to device Vulkan0`) to confirm
  the GPU runs really used the GPU.

### 3.3 Limitations
- **Single runs, no repeats** in sections 4 and 5; expect a few percent of noise and more on short outputs
  (the 9-12 token answers give unreliable t/s). Section 6 repeats the task benchmark with three seeds, and 6.13 extends it to 40 tasks and five seeds.
- **Swap was nearly full** during the 9B runs, which depresses prefill and probably
  generation. Results with more free RAM could be better.
- Sections 4.2-4.4 judged quality by reading three short answers; the task benchmark (sections 5-6) replaced that with graded tests, but it was only 11 questions. 6.13 extends it to 40 tasks (regex 8, Python 12, kubectl 10, SQL 5, shell 5) and five seeds; even so it is a small, home-made suite, not a standard benchmark.
- Thinking-on behaviour was not compared between models; all benchmark runs use thinking off.

### 3.4 How the score is calculated

Two scales are used. Sections 5-6.11 score the original 11 tasks (maximum 11, seeds 42-44). Section 6.13 and the deck's later pages score the extended suite: **maximum 40**
(the 11 original tasks plus 29 new ones: regex +5, Python +8, kubectl +6, SQL +5, shell +5), seeds 42-46, so one task is 2.5% of the score and the table shows the mean ± SD of five scores
(for example Qwen 3B: 28, 30, 29, 28, 25 -> 28.0 ± 1.9). SQL tasks are graded by running the query with `sqlite3` on a fixture database (SELECT only, rows compared); shell tasks by running the command in a bubblewrap sandbox
(no network, throw-away files) and comparing its output. The rest of this section describes the original 11-task scoring, which the extended suite extends unchanged.

- **Maximum 11 (original set).** The task benchmark has 11 tasks (3 regex, 4 Python, 4 kubectl). Each is worth 1 point, pass or fail, with no partial credit; a task
  passes only if a hidden grader accepts the whole answer (section 5, questions in 6.1).
- **Graders.** Regex: `re.fullmatch` must accept every must-match string and reject every must-reject string. Python: the extracted code runs in a fresh
  `python3 -I` process and every assertion must hold (including a 200,000-number timing test for `py-lis`). kubectl: every required verb, resource, name,
  flag and value must be present in the command (quotes ignored; no cluster is contacted).
- **Seeds.** A seed is the starting value of the random number generator that picks each next token. At temperature 0.6 the model samples, so the same prompt can give
  different answers; a fixed seed makes a run reproducible, and a different seed (42, 43, 44) is a different random draw with the same model, questions and settings.
  Each model is run once per seed, giving three scores out of 11; the tables show their mean ± SD (for example Qwen 3B: 7, 8, 8 -> 7.7 ± 0.6).
  The spread shows how much sampling alone moves a score (MiMo: 9, 6, 7). Three seeds is few, so the results are a smoke test, not a ranking.
- **Harness columns.** "No harness" is the first attempt. "+1 / +2 retries" is the answer after the verify -> retry loop (6.3). Both are graded by the same hidden
  tests, and the first attempt uses the same seed as a naked run, so the two columns are paired.
- **Resolution.** One question is 1/11 = 0.09 of the score, so differences of about one point are inside the seed-to-seed noise.
- **Caveat.** We wrote the graders and fixed bugs in them (5.4, 6.7); saved answers were re-graded after each fix.

## 4. Results

### 4.1 Tuning experiments (Qwen2.5-Coder-3B-Instruct Q4_K_M, ~1.9 GB)

| Configuration | Prefill t/s | Generation t/s |
|---|---:|---:|
| CPU, 4 threads (baseline) | 65-78 | **10.7** |
| CPU, 8 threads | 69 | 8.7 |
| CPU, 3 / 6 threads | 76 / 81 | 10.5 / 10.5 |
| CPU, flash attention | 77 | 10.7 |
| CPU, flash attention + q8 KV cache | 68 | 10.7 |
| CPU, `--no-mmap` | 76 | 10.7 |
| CPU, larger batch (`-b 2048`) | 76 | 10.6 |
| GPU (Vulkan, all layers) | 65-86 | 6.2-6.7 |
| CPU + 0.5B draft model | n/a | 7.4 (43% draft acceptance) |
| CPU + n-gram speculation | n/a | 11.1 |

Takeaways:
- Generation is bandwidth-saturated at ~10.7 t/s (about 20 GB/s effective); software flags
  do not move it.
- 4 threads beat 8: hyperthreads compete for bandwidth.
- The iGPU is functional but loses to the CPU for generation and only matches it at prefill.
- A mismatched draft model *hurts*: low acceptance makes verification pure overhead.

### 4.2 Ornith 1.5 9B (Q4_K_M, 5.8 GB)

| Configuration | Prefill t/s | Generation t/s |
|---|---:|---:|
| CPU, 4 threads, no speculation | 25.8 | 3.7 |
| GPU (Vulkan) | 26.6 | 2.3 |
| MTP build, no speculation | 7.4* | 3.7 |
| MTP build, `draft-mtp`, default draft length | 9.9* | 3.9 (47% acceptance) |
| MTP build, `--spec-draft-n-max 1` | 11.2* | **4.7** |
| MTP build, `--spec-draft-n-max 2` | 9.1* | **4.7** |

\* Measured while swap was nearly full; prefill figures in this block are not comparable
with the first two rows.

Ornith 1.5 ships without MTP weights in the stock GGUFs; the `protoLabsAI/...-MTP-GGUF`
build bakes a multi-token-prediction head into the file. With a short draft (1-2 tokens)
it gives +27% generation speed at no extra memory cost. Longer drafts lose their benefit.

### 4.3 Ornith vs MiMo (both ~9B, Q4_K_M, thinking off)

| Prompt | MiMo V2.6 Distill Qwen 9B | Ornith 1.5 9B + MTP |
|---|---:|---:|
| Python interval-merge function (200 tok) | 3.5 t/s | 5.1 t/s |
| Sky-is-blue, 3 sentences (66-81 tok) | 3.2 t/s | 4.2 t/s |
| Train duration (9-12 tok) | 1.6 t/s | 1.7 t/s |

| | MiMo V2.6 Distill Qwen 9B | Ornith 1.5 9B |
|---|---|---|
| GGUF used | `bartowski/...-GGUF` Q4_K_M, 5.8 GB | `protoLabsAI/...-MTP-GGUF` Q4_K_M, 5.8 GB |
| Speculative decoding | none available | built-in MTP head |
| Speed (longer answers) | 3.2-3.5 t/s | 4.2-5.1 t/s (**~30-45% faster**) |
| Answer quality (3 prompts) | Correct and well structured | Correct and well structured |
| Reasoning mode | `enable_thinking` switch | Reasoning model; `<think>` opens by default, same switch |
| Recommended sampling | not found in model card | temp 1.0 / presence 1.5 (general), temp 0.6 (coding) |

The speed gap comes almost entirely from MTP: the two files are the same size and the
bandwidth ceiling is identical. Output quality was indistinguishable on these three prompts.

### 4.4 Nemotron 3 Nano 4B (Q4_K_M, 2.8 GB, thinking off)

`lmstudio-community/NVIDIA-Nemotron-3-Nano-4B-GGUF`, same 3 prompts, CPU, 4 threads, no speculation.

| Prompt | Nemotron 3 Nano 4B | Ornith 9B + MTP | MiMo 9B |
|---|---:|---:|---:|
| Python interval-merge function (200 tok) | 6.1 t/s | 5.1 t/s | 3.5 t/s |
| Sky-is-blue, 3 sentences | 5.7 t/s | 4.2 t/s | 3.2 t/s |
| Train duration (13 tok) | 3.3 t/s | 1.7 t/s | 1.6 t/s |

- About 20-70% faster than the 9B models, yet **well below** the ~12 t/s bandwidth ceiling for
  2.8 GB (and below the 10.7 t/s of the 3B Qwen coder at 1.9 GB). Against the ~20 GB/s effective bandwidth the 3B reaches, the ceiling for 2.8 GB is
  about 7 t/s, so 5-6 t/s is 70-85% of it: the hybrid state-space/attention design may cost some speed on CPU kernels, but the evidence for that is weak.
- Answers were correct and well formed on all three prompts, comparable to the 9B models.
- Run with `make run-nemotron`.

## 5. Task benchmark (regex, Python, kubectl)

`make benchmark` runs 11 fixed questions on every model: 3 regex, 4 Python algorithms and
4 kubectl commands. Every answer is saved in its own file, `benchmarks/results/<model>/<question>.md`
(with a `.json` of metadata), and graded automatically. `benchmarks/results/SUMMARY.md` is rebuilt
by `make benchmark-summary`.

**Setup.** Q4_K_M GGUFs, CPU, 4 threads, 4k context. Same request for every model: temperature 0.6,
top_p 0.95, top_k 20, seed 42, `max_tokens` 512, **thinking requested off**
(`enable_thinking=false`). No model produced any reasoning text and none was cut off at the token limit.

**Grading** (`benchmarks/run.py`):
- *regex*: the pattern from the code block is compiled and used with `re.fullmatch` against 3-4 strings
  that must match and 5-6 that must not.
- *Python*: the function is extracted and run in a fresh `python3 -I` process against assertions;
  `lis_length` is also run on 200,000 elements and must finish within 5 s and agree with a reference.
- *kubectl*: the command must contain every required part (verb, resource, namespace, flags), in any order.

### 5.1 Summary by model

| Model | Size | Regex | Python | kubectl | **Total** | Avg speed | Avg time per answer |
|---|---:|:---:|:---:|:---:|:---:|---:|---:|
| Ornith 1.5 9B + MTP | 5.8 GB | 3/3 | 3/4 | 3/4 | **9/11** | 3.2 t/s | 29 s |
| MiMo V2.6 Distill Qwen 9B | 5.8 GB | 3/3 | 3/4 | 3/4 | **9/11** | 2.9 t/s | 21 s |
| Nemotron 3 Nano 4B | 2.8 GB | 2/3 | 4/4 | 2/4 | **8/11** | 5.2 t/s | 10 s |
| Qwen2.5-Coder 3B | 1.9 GB | 0/3 | 3/4 | 4/4 | **7/11** | 8.3 t/s | 6 s |

Speeds here are wall-clock averages over short answers (20-110 tokens), so they include prompt
processing and are lower than the steady-state figures in section 4.

### 5.2 Detailed results, question by model

| Question | Ornith 9B + MTP | MiMo 9B | Nemotron 4B | Qwen2.5-Coder 3B |
|---|---|---|---|---|
| regex-ipv4 | PASS | PASS | PASS | FAIL: accepts 256.x and 300.x |
| regex-date | PASS | PASS | FAIL: no month/day range check | FAIL: no month/day range check |
| regex-hexcolor | PASS | PASS | PASS | FAIL: `{3,6}` accepts 4 and 5 digits |
| py-intervals | PASS | PASS | PASS | PASS |
| py-lis (O(n log n)) | PASS | FAIL: missing `import bisect`, broken bookkeeping | PASS | FAIL: O(n²) DP, times out |
| py-topk | FAIL: ignores the alphabetical tie-break | PASS | PASS | PASS |
| py-coins | PASS | PASS | PASS | PASS |
| kubectl-pods-sorted | PASS | FAIL: invented `--sort=` flag | FAIL: jsonpath/`sort` pipe, no `--sort-by` | PASS |
| kubectl-scale | PASS | PASS | PASS | PASS |
| kubectl-logs | FAIL: `api-0/app` instead of `-c app` | PASS | FAIL: no `-c app`, no `-f` | PASS |
| kubectl-nodes-names | PASS | PASS | PASS | PASS |
| **Total** | **9/11** | **9/11** | **8/11** | **7/11** |

### 5.3 What the benchmark shows

- **Quality does not clearly scale with size.** In this single run the two 9B models tie at 9/11 and the 4B and 3B follow,
  but the gaps are 1-2 questions, which is within what another prompt set could reverse.
  *(Section 6.4: this run is seed 42 of three. Over three seeds the means are Ornith 9.0, Nemotron 8.0,
  Qwen 7.7, MiMo 7.3, so the tie was one draw, and the 7B Qwen (8.0, added later) equals the 4B Nemotron while the 9B MiMo is below the 3B Qwen: size does not predict the score here.)*
- **The failures differ by model, not by task type.** Qwen2.5-Coder 3B fails every regex question
  (patterns that are too loose) yet gets all four kubectl commands; the larger models make small
  command mistakes (invented flags, wrong container syntax) but write correct regexes.
  *(Section 6.4: this holds for seed 42 only. Qwen's regex scores over the three seeds are 0, 3 and 2 of 3,
  and its kubectl scores 4, 3 and 3 of 4. Nemotron's kubectl failures, by contrast, repeat on every seed.)*
- **Instruction following.** MiMo returned code without a code fence in several answers, and its
  answers are graded as if fenced; this was counted as a format slip, not a failure.
- **Speed vs score.** Nemotron 4B scored 8/11 at 5.2 t/s against 9/11 at ~3 t/s for the 9B models,
  and Qwen2.5-Coder 3B 7/11 at 8.3 t/s. For short factual or command-style tasks the smaller models
  give most of the quality in a third of the time.
- **Caveats.** One run per cell, 11 questions, temperature 0.6 with a fixed seed. A single flipped
  answer moves a model by 9 percentage points of its total. Treat the table as a smoke test, not a ranking.

### 5.4 Grader corrections made during the run

Two issues in the grading, not the models, were found by reading the failures and fixed, then all
saved answers were re-graded without re-running any model:
- the `lis_length` test asserted a wrong range for the expected result on random data
  (it is about 880, not 1000-2000); it now compares against a reference implementation;
- unfenced code and `r'...'`-wrapped regexes were being rejected; both are now accepted.

A third issue was found later, in the section 6 runs: the kubectl check rejected a correct command when a flag
value was quoted (`--sort-by='.metadata.creationTimestamp'`). Quote characters are now ignored when matching.
Re-grading all saved answers changed exactly 3 attempts, all in section 6, and none of the section 5 results.

### 5.5 Excluded: DeepSeek-R1-0528-Qwen3-8B

It was downloaded and started but dropped. It always opens a reasoning trace, `enable_thinking=false`
did not stop it, and on its first question it used all 512 tokens without producing an answer, at
about 4 t/s. Running it with thinking would take far too long on this machine, so the model file
was deleted.

## 6. Stability and harness experiment

Section 5 was a single run per question. This section repeats it to measure run-to-run variation,
and adds a *harness* around the model to see how much of the remaining error is fixable cheaply.

### 6.1 Questions

1. **Stability**: if the same model answers the same 11 questions again with a different random
   seed, does its score move, and which questions flip?
2. **Harness**: the failures in section 5 are mostly mechanically checkable (a regex that accepts
   `300.1.1.1`, an invented `kubectl` flag, a function that times out). Does a
   generate -> verify -> retry-with-feedback loop recover them without a larger model?

### 6.2 Design

- **Seeds.** Every question is run with seeds 42, 43 and 44 (temperature 0.6, top_p 0.95, top_k 20, 4k context,
  thinking off, as in section 5). The seed has to differ between runs: with one fixed seed the repeats
  would be near-identical and would say nothing about stability. Seed 42 matches section 5.
- **Clean re-run, not a reuse.** The section 5 answers were not reused. The machine had just been rebooted
  when these runs started (uptime about 5 min, swap empty, ~13 GB available), whereas the section 4/5
  runs had swap almost full, so speeds may differ from sections 4 and 5. In the end the average speeds
  agreed with section 5.1 for three models (see 6.4). Start conditions are saved per batch in
  `runs/<mode>/<model>/conditions.json`.
- **Paired design.** In harness mode the first attempt is the same request as a naked run (same prompt, seed
  and parameters; prompt caching is switched off for every request). It is graded by the hidden tests
  and stored, so one harness run contains the naked result for that seed and the harnessed result for
  the same seed. For MiMo, Nemotron and Qwen the "no harness" columns are these first attempts.
- **Ornith** was run naked first (3 seeds), and then through the same harness as a last step, to compare
  it with the other models. Its first harness attempts also repeat its naked runs, which doubles as a
  determinism check for the fixed-seed setup.
- **Retry budget.** Up to 2 retries were allowed. The first retry only depends on the first attempt, so the same
  transcripts give both "+1 retry" and "+2 retries". Each retry is a new turn in the same conversation:
  the previous answer, then *"That answer failed verification: <reason>. Fix it. Reply with ONLY the
  corrected <regex | code | command> in a code block."*
- **Grading is unchanged.** Every attempt is graded by the hidden tests from section 5; the verifier
  never decides the score.

### 6.3 The harness and its verifier

The verifier must not see the answer key. If it ran the hidden strings and assertions, the result would
measure a perfect oracle, not a realistic tool. It uses a separate set of **public examples**
(`benchmarks/public.json`), written for this experiment and disjoint from the hidden cases:

| Task type | Verifier | Feedback given to the model |
|---|---|---|
| regex (3) | 3 strings that must match and 4-5 that must not, via `re.fullmatch` | which strings it wrongly accepts or rejects; or the compile error |
| Python (4) | 3-4 public calls with expected values, run in a fresh `python3 -I` process; `lis_length` also gets a 20,000-element timing check (limit 2 s) | the failing call with returned vs expected value, the exception, or "too slow" |
| kubectl (4) | the real `kubectl` argument parser, offline (the runs in 6.4-6.8); a task-requirements check was added afterwards, see 6.9 | `error: unknown flag: --sort`, wrong argument count, or "not a single command" (6.9 adds e.g. "the container to read should be `app`") |

- **kubectl isolation.** Model output is never run through a shell. The command is split with `shlex`,
  pipes, redirects and substitutions are refused, and it runs under `unshare -rn` (no network at all),
  with a dummy kubeconfig pointing at an unreachable address, a temporary `HOME` and a `PATH` that contains only `kubectl`.
  A syntactically valid command then fails with "network is unreachable", which is read as *accepted*;
  a rejected flag or argument is reported back. No cluster is involved (this replaces the `--dry-run` idea
  from the TODO, since `--dry-run` still needs a server for `get` and `scale`).
- **What it cannot see.** The kubectl check validates syntax only. A command that parses but is semantically
  wrong (`logs api-0/app` instead of `-c app`, a missing `-f`) passes. The public regex and Python examples
  are also few; an answer can satisfy them and still fail the hidden tests. Both cases are counted
  below as "verifier OK but hidden test failed".
- **Checked before use.** The verifiers were run on 20 hand-written good and bad answers (loose and exact IPv4 regex,
  `{3,6}` hex colour, O(n^2) vs O(n log n) LIS, missing tie-break, syntax errors, invented kubectl flag,
  piped command, two commands, non-kubectl command) and all 20 behaved as intended.

### 6.4 Results: stability without harness

Scores are hidden-test passes out of 11 on the **first attempt** (no harness), for seeds 42 / 43 / 44. Ornith comes
from its naked runs; the other models from the first attempts of their harness runs (see 6.2).

| Model | Score per seed | Mean ± SD | Questions always / never / flaky | Best of 3 seeds | Speed, t/s (mean ± SD over seeds) |
|---|---|---|---|---:|---|
| Ornith 1.5 9B + MTP | 9 / 10 / 8 | 9.0 ± 1.0 | 8 / 1 / 2 | 10 | 3.9 ± 0.1 |
| Nemotron 3 Nano 4B | 8 / 8 / 8 | 8.0 ± 0.0 | 8 / 3 / 0 | 8 | 5.2 ± 0.0 |
| Qwen2.5-Coder 3B | 7 / 8 / 8 | 7.7 ± 0.6 | 5 / 1 / 5 | 10 | 8.3 ± 0.3 |
| Qwen2.5-Coder 7B | 8 / 8 / 8 | 8.0 ± 0.0 | 8 / 3 / 0 | 8 | 3.4 ± 0.1 |
| MiMo V2.6 Distill Qwen 9B | 9 / 6 / 7 | 7.3 ± 1.5 | 5 / 2 / 4 | 9 | 3.0 ± 0.1 |

*Always / never / flaky* count the questions that passed in all three seeds, in none, or in some. *Best of 3* is the number of
questions passed at least once. Speed is wall-clock tokens per second per answer (prompt processing included).

By category, mean ± SD over the seeds:

| Model | regex (3) | Python (4) | kubectl (4) |
|---|---|---|---|
| Ornith | 3.0 ± 0.0 | 2.7 ± 0.6 | 3.3 ± 0.6 |
| Nemotron | 2.0 ± 0.0 | 4.0 ± 0.0 | 2.0 ± 0.0 |
| Qwen | 1.7 ± 1.5 | 2.7 ± 0.6 | 3.3 ± 0.6 |
| Qwen 7B | 2.0 ± 0.0 | 2.0 ± 0.0 | 4.0 ± 0.0 |
| MiMo | 2.0 ± 1.0 | 2.3 ± 0.6 | 3.0 ± 0.0 |

Per question, passes over the three seeds (`*` = flaky):

| Question | Ornith | Nemotron | Qwen | Qwen 7B | MiMo |
|---|---|---|---|---|---|
| regex-ipv4 | 3/3 | 3/3 | 2/3* | 3/3 | 2/3* |
| regex-date | 3/3 | 0/3 | 1/3* | 0/3 | 2/3* |
| regex-hexcolor | 3/3 | 3/3 | 2/3* | 3/3 | 2/3* |
| py-intervals | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| py-lis | 2/3* | 3/3 | 0/3 | 0/3 | 0/3 |
| py-topk | 0/3 | 3/3 | 2/3* | 0/3 | 1/3* |
| py-coins | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| kubectl-pods-sorted | 3/3 | 0/3 | 3/3 | 3/3 | 0/3 |
| kubectl-scale | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| kubectl-logs | 1/3* | 0/3 | 1/3* | 3/3 | 3/3 |
| kubectl-nodes-names | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |

What it shows:

- **Section 5 is reproduced exactly.** Seed 42 gives the same pass/fail outcome as the single run of section 5 in all
  44 cells (4 models x 11 questions), although the two runs were hours apart in different machine states. Ornith's
  first harness attempts are identical to its naked answers in 33 of 33 cells, and the one cell that had to be re-run
  (see 6.7) gave the identical answer. With a fixed seed the setup is deterministic, so everything that differs between
  seeds is sampling, not machine noise. Section 5 was one draw from this spread.
- **The ranking of section 5 does not survive.** Section 5 had Ornith = MiMo (9) > Nemotron (8) > Qwen (7). Over three
  seeds it is Ornith 9.0 > Nemotron 8.0 > Qwen 7.7 > MiMo 7.3: MiMo's 9/11 was its best seed (it scored 6 and 7 on the
  others). The gaps between the last three (at most 0.7) are smaller than their SDs (up to 1.5), so their order is not
  established. Ornith's lead over MiMo (1.7 questions; SDs 1.0 and 1.5, Welch t about 1.6, p about 0.2 with three seeds) is not statistically established: the direction is consistent with the other results but the evidence is weak.
- **A stable total can hide a lot of churn, and a stable model can be stably wrong.** Qwen scores 7, 8, 8, yet 5 of its 11
  questions flip between seeds (the failures just change places). Nemotron has no flips at all, but the same three
  questions (`regex-date`, `kubectl-pods-sorted`, `kubectl-logs`) fail on every seed. Qwen and MiMo are *random*
  failures (another sample may be right); Nemotron's are *systematic* (resampling will not help; feedback might).
- **Small models are least stable on regexes.** Qwen's regex score per seed is 0, 3, 2 of 3 and MiMo's 3, 1, 2. The
  section 5 statement that Qwen fails every regex but gets all four kubectl commands was true of seed 42 only: its
  kubectl scores are 4, 3, 3 of 4.
- **Speed is the stable quantity.** The SD across seeds is at most 0.3 t/s. The averages agree with section 5.1 for
  three models (Nemotron 5.2 vs 5.2, Qwen 8.3 vs 8.3, MiMo 3.0 vs 2.9); only Ornith is faster (3.9 vs 3.2, +22%), which fits
  the nearly full swap during section 5.

### 6.5 Results: with the harness

Score = hidden-test passes out of 11 per seed, mean ± SD over seeds (per-seed scores in brackets). A *cell* is one
(question, seed) pair: 33 per model, 132 in total. Time cost = seconds for all attempts / seconds for first attempts only.

These numbers use the kubectl verifier with task requirements (6.9). The first harness run used a syntax-only kubectl
verifier; only the 4 kubectl questions were re-run, the other 7 are unchanged, and the comparison is in 6.9.

| Model | No harness | +1 retry | +2 retries | Answers rejected by the verifier, per run | Cells fixed | Cells broken | Verifier OK but hidden test failed | Time cost |
|---|---|---|---|---|---:|---:|---:|---|
| Ornith | 9.0 ± 1.0 (9/10/8) | 10.7 ± 0.6 (11/11/10) | 10.7 ± 0.6 (11/11/10) | 2.0 ± 1.0 | 5 | 0 | 0 | x1.30 |
| MiMo | 7.3 ± 1.5 (9/6/7) | 9.0 ± 0.0 (9/9/9) | 10.0 ± 1.0 (9/11/10) | 3.7 ± 1.5 | 8 | 0 | 0 | x1.95 |
| Qwen | 7.7 ± 0.6 (7/8/8) | 8.7 ± 1.2 (8/8/10) | 9.3 ± 1.2 (10/8/10) | 3.0 ± 1.0 | 5 | 0 | 1 | x1.70 |
| Qwen 7B | 8.0 ± 0.0 (8/8/8) | 10.0 ± 0.0 (10/10/10) | 10.0 ± 0.0 (10/10/10) | 3.0 ± 0.0 | 6 | 0 | 0 | x1.57 |
| Nemotron | 8.0 ± 0.0 (8/8/8) | 8.7 ± 0.6 (9/9/8) | 8.7 ± 0.6 (9/9/8) | 3.0 ± 0.0 | 2 | 0 | 0 | x1.50 |

Per question, passes without harness -> +1 retry -> +2 retries (over the three seeds):

| Question | Ornith | MiMo | Qwen | Qwen 7B | Nemotron |
|---|---|---|---|---|---|
| regex-ipv4 | 3 -> 3 -> 3 | 2 -> 2 -> 2 | 2 -> 2 -> 3 | 3 -> 3 -> 3 | 3 -> 3 -> 3 |
| regex-date | 3 -> 3 -> 3 | 2 -> 2 -> 3 | 1 -> 1 -> 1 | 0 -> 3 -> 3 | 0 -> 1 -> 1 |
| regex-hexcolor | 3 -> 3 -> 3 | 2 -> 3 -> 3 | 2 -> 2 -> 3 | 3 -> 3 -> 3 | 3 -> 3 -> 3 |
| py-intervals | 3 -> 3 -> 3 | 3 -> 3 -> 3 | 3 -> 3 -> 3 | 3 -> 3 -> 3 | 3 -> 3 -> 3 |
| py-lis | 2 -> 2 -> 2 | 0 -> 1 -> 2 | 0 -> 2 -> 2 | 0 -> 3 -> 3 | 3 -> 3 -> 3 |
| py-topk | 0 -> 3 -> 3 | 1 -> 2 -> 3 | 2 -> 2 -> 2 | 0 -> 0 -> 0 | 3 -> 3 -> 3 |
| py-coins | 3 -> 3 -> 3 | 3 -> 3 -> 3 | 3 -> 3 -> 3 | 3 -> 3 -> 3 | 3 -> 3 -> 3 |
| kubectl-pods-sorted | 3 -> 3 -> 3 | 0 -> 2 -> 2 | 3 -> 3 -> 3 | 3 -> 3 -> 3 | 0 -> 1 -> 1 |
| kubectl-scale | 3 -> 3 -> 3 | 3 -> 3 -> 3 | 3 -> 3 -> 3 | 3 -> 3 -> 3 | 3 -> 3 -> 3 |
| kubectl-logs | 1 -> 3 -> 3 | 3 -> 3 -> 3 | 1 -> 2 -> 2 | 3 -> 3 -> 3 | 0 -> 0 -> 0 |
| kubectl-nodes-names | 3 -> 3 -> 3 | 3 -> 3 -> 3 | 3 -> 3 -> 3 | 3 -> 3 -> 3 | 3 -> 3 -> 3 |

What it shows:

- **It helps every model and never made an answer worse**: 20 of 132 cells fixed, 0 broken. At two retries the means
  are Ornith 10.7, MiMo 10.0, Qwen 9.3, Nemotron 8.7, i.e. gains of +1.7, +2.7, +1.6 and +0.7 questions.
- **Most of the gain comes from the first retry.** The second retry adds +1.0 for MiMo and +0.6 for Qwen and nothing for
  Ornith or Nemotron. Allow two.
- **The weakest naked model gains most.** MiMo's errors are mechanical and visible to the verifier: missing imports
  (`bisect`, `bisect_left`, `collections`, `Counter`, causing a `NameError` in `py-lis` and `py-topk`), an invented
  `kubectl --sort` flag, a month pattern that accepts 13-31. Its 8 fixed cells are `py-lis` 2, `py-topk` 2,
  `kubectl-pods-sorted` 2, `regex-date` 1, `regex-hexcolor` 1. With two retries it reaches Ornith's level.
- **Ornith benefits too.** Its 5 fixed cells are `py-topk` 3 and `kubectl-logs` 2. `py-topk` fails 0/3 without feedback (a wrong
  alphabetical tie-break in one seed, a duplicated word in the other two) and passes 3/3 after one retry; `kubectl-logs`
  (`api-0/app` instead of `-c app`) is fixed in 2 of its 3 seeds once the verifier checks the container. The TODO assumed Ornith could skip
  the harness because it builds its own scaffold; used as a plain chat model it does not, and the external loop gave +1.7.
- **Nemotron gains least, and a better verifier did not change that.** Its `kubectl-logs` is always a valid command that omits
  `-c app` (`api-0/app`, `-n api-0`), and `kubectl-pods-sorted` ends as `--sort-by=createTime` or `--sort-by=creationTimestamp`.
  The first run's verifier accepted these (5 of its 33 cells); the stronger one rejects all of them (6 of the 12 kubectl first attempts rejected
  over the three seeds, instead of 2) and says what is wrong, yet the final scores are the same, because Nemotron repeats the command: 8 of its 16 retries were
  identical to the previous attempt (`kubectl-logs` seed 44: the same command three times).
- **The kubectl verifier was the weak point, and is fixed.** With the syntax-only verifier all 9 "verifier OK but hidden test
  failed" cells were kubectl (`kubectl-logs` 7, `kubectl-pods-sorted` 2). With the requirements check there is 1 such cell
  (Qwen `kubectl-logs` seed 43, `logs api-0 app`, valid kubectl that the hidden regex wrongly refuses, see 6.9). The regex and
  Python checks produced no blind spots; the cases that stay wrong there are ones where the model does not act on correct
  feedback (see 6.6).
- **Still wrong after two retries**, in cells: Ornith `py-lis` 1; MiMo `py-lis` 1, `kubectl-pods-sorted` 1,
  `regex-ipv4` 1; Qwen `regex-date` 2, `kubectl-logs` 1, `py-lis` 1, `py-topk` 1; Nemotron `kubectl-logs` 3,
  `kubectl-pods-sorted` 2, `regex-date` 2.
- **Cost.** Time grows by x1.30 (Ornith) to x1.95 (MiMo), because most cells need no retry (accepted on the first attempt:
  Ornith 27 of 33, Nemotron 24, Qwen 24, MiMo 22) but a retry costs a full extra generation, longer than the first one
  for three models (mean tokens first attempt -> retry: MiMo 59 -> 89, Qwen 69 -> 92, Ornith 62 -> 67; Nemotron is the exception,
  52 -> 32). For all 33 cells MiMo needed 1195 s against 614 s for its first attempts; its slowest cell took 191 s.
- **Time per quality.** Over the 33 cells, Qwen with harness reached 9.3/11 in 419 s, a little above what Ornith reached naked
  (9.0/11 in 469 s, first attempts only). Ornith with harness reached 10.7 in 612 s, MiMo with harness 10.0 in 1195 s.

**Where the gain comes from, and what it is not** (computed afterwards from `benchmarks/runs/STATS.md`, all five models).
- **By task type.** Of the 26 cells fixed, 20 are regex or Python and 6 are kubectl. Of the 32 regex/Python cells that failed on the first attempt, 20 were fixed
  (62%); of the 13 failed kubectl cells, 6 (46%). The regex and Python checks (public examples, assertions) are independent of the hidden tests, so that gain is
  credible: about +1.0 (Ornith), +2.0 (MiMo, 7B), +1.3 (3B) and +0.3 (Nemotron) questions per run. The kubectl verifier was written from the task requirements and is close to an
  oracle (6.9), so the kubectl part (up to +0.7 per run) is an upper bound for a user who must write such checks for each task.
- **Control arm (run afterwards): the feedback adds little.** For every first attempt the verifier rejected, the control arm retried with a *fresh sample of the original
  prompt (new seed) and no feedback*, up to two times, with the same verifier deciding when to stop (`python3 benchmarks/repeat.py --mode resample`, results in
  `benchmarks/runs/resample/`, table in `runs/RESAMPLE.md`). The first attempts are the harness's own, so the comparison is paired. Score /11, mean ± SD over three seeds:

| Model | No retry | + 2 retries with feedback (harness) | + 2 retries without feedback (control) | Cells fixed: feedback / control |
|---|---|---|---|---|
| Ornith | 9.0 ± 1.0 | 10.7 ± 0.6 | 11.0 ± 0.0 | 5 / 6 |
| MiMo | 7.3 ± 1.5 | 10.0 ± 1.0 | 8.3 ± 1.2 | 8 / 3 |
| Qwen 3B | 7.7 ± 0.6 | 9.3 ± 1.2 | 10.0 ± 0.0 | 5 / 7 |
| Qwen 7B | 8.0 ± 0.0 | 10.0 ± 0.0 | 9.7 ± 0.6 | 6 / 5 |
| Nemotron | 8.0 ± 0.0 | 8.7 ± 0.6 | 9.3 ± 0.6 | 2 / 4 |
| **All** | | | | **26 / 25** (broken 0 / 0) |

  By task type (cells fixed with / without feedback): regex and Python 20 / 19, kubectl 6 / 6.
- **Reading it.** Overall the control fixed 25 of 45 failed cells against 26 with feedback, so on this task set **most of the harness gain comes from verify-and-resample,
  not from the feedback text**: the verifier tells the loop *that* an answer is wrong, and a second or third draw from a model that is right about half the time often is right.
  Feedback clearly helped only MiMo (8 against 3 cells, 10.0 against 8.3 questions), whose mistakes are mechanical (a missing import, a missing code fence). For Ornith, Qwen 3B and Nemotron the
  control scored as high or higher (the differences, 0.3 to 1.3 questions, are within the seed-to-seed spread, so they show no feedback benefit rather than a feedback harm). Nemotron, which
  repeats its command after feedback, did better when simply asked again (9.3 against 8.7). The rough estimate above (about 13 fixes from resampling) was too low:
  the measured figure is 25.
- **What this does not say.** A verifier is still needed: it decides which answers to redraw, and the kubectl one is close to an oracle (6.9). The retry budget is small (two draws), the control
  uses new seeds, so each control retry is one sample from the model's distribution, and three seeds per model limit what any per-model difference can show. Feedback may matter more for tasks
  where the model cannot reach the answer by luck (here a question that never passed, such as Qwen 7B `py-topk`, stayed at 0/3 in both arms).

### 6.6 Models run behaviour

Observations from the saved transcripts (`runs/<mode>/<model>/seed<N>/<question>.md`).

**Thinking was off.** Every request carries `enable_thinking=false`, and no transcript contains a `<think>` tag.
Only 1 of 220 attempts (33 naked + 187 harness) hit the 512-token limit. The server's own `reasoning_content` was
not saved in the batch runs, so it was checked directly afterwards with one short request per model, thinking off
and thinking on as a control:

| Model | Thinking off: reasoning text | Thinking on (control) |
|---|---|---|
| Ornith | 0 chars (4 tokens) | 14 chars (20 tokens): the flag works |
| Nemotron | 0 chars (12 tokens) | 92 chars (42 tokens): the flag works |
| MiMo | 0 chars (4 tokens) | 0 chars (6 tokens): no visible effect on this prompt |
| Qwen2.5-Coder | 0 chars (12 tokens) | 0 chars, identical output: this model has no thinking mode |

For MiMo the check shows that no reasoning text was produced, but not that the switch does anything. The runner now
records `reasoning_chars` per attempt (it was 0 for the re-run cell).

**How the models react to feedback.**

- **A retry is often a new answer, but not always.** 17 of the 55 retries (31%) returned the identical code block
  (Ornith 2 of 7, Nemotron 8 of 16, Qwen 3 of 15, MiMo 4 of 17). 20 of the 55 retries passed the hidden tests.
  Examples of feedback being ignored: Ornith `py-lis` seed 44 returned the same `IndexError` code three times;
  Qwen `py-topk` seed 43 returned the same tie-break bug three times although the feedback quoted the failing call
  (`top_k_frequent(['dog','cat','cat','dog'],1) returned ['dog'], expected ['cat']`); Nemotron `regex-date` seed 44
  returned the same regex three times.
- **Ornith** acts on precise feedback best: its `py-topk` error (tie-break, or a duplicated word) was fixed in one retry on
  every seed. Its `kubectl-logs` first answer (`kubectl logs -f api-0/app --tail=100`) is the same in two seeds; with the requirements check the
  verifier says the container is missing and the retry in both seeds is `kubectl logs -f pod/api-0 -c app --tail=100`, which passes
  (5 of its 7 retries passed in total).
- **MiMo** forgets imports (a `NameError` on the first attempt of several `py-lis` and `py-topk` cells) and often
  returns code with no fence; both are repaired after feedback. Its feedback reactions can be long-winded: seed 43,
  `regex-date`, attempt 1 used the day pattern for the month as well. The verifier reported that `2023-15-10` was wrongly
  accepted. Attempt 2 repeated the same regex and then wrote about 500 tokens of self-doubt in the answer itself ("Wait -
  `15` is already rejected by `3[01]`... Hmm, but the user says it fails verification...", concluding the verifier was
  wrong), and was cut off at 512 tokens after 141 s. Attempt 3 put `(0[1-9]|1[0-2])` in the month and passed. Thinking was off
  throughout, so this is ordinary visible text; the question cost 191 s against about 15 s when it works first time.
- **Qwen** changes its answer but does not always converge. `regex-date` seed 42: `\d{4}-\d{2}-\d{2}`, then a month pattern
  `([01][0-9]|2[0-2])`, then `([01]\d|[2][0-3])`, still wrong after two retries. `regex-ipv4` seed 42: the same loose regex
  twice, then a correct 0-255 pattern. `py-lis` seed 43: an O(n^2) solution (too slow), then the right algorithm
  without `import bisect`, then an `IndexError`.
- **Nemotron** answers "sorted by creation timestamp" with `jsonpath`, `jq` or `sort` pipes instead of `--sort-by`; the verifier
  refuses pipes. In one seed the retry produced a correct `--sort-by='.metadata.creationTimestamp'`; in the others the answer
  ended as `--sort-by=createTime` or `--sort-by=creationTimestamp`, valid syntax with the wrong field. The stronger verifier
  rejects these ("sort expression found: 'createTime'") but the model returns the same command (seed 44: `--sort-by=creationTimestamp`
  three times). Its answers get shorter on retry (52 -> 32 tokens on average), the opposite of the other models.

### 6.7 Limitations and incidents

- **Three seeds.** A standard deviation from 3 values is only a rough indication, and 11 questions give
  coarse scores (one question is 9 percentage points of the total). "Flaky" means a question gave different outcomes across
  the three seeds; a question that passed 3/3 is not proven stable.
- **The public examples were written by us**, after seeing the section 5 failures. They are plausible
  user-supplied examples, but a different set would give different retry outcomes. The harness numbers show
  what a verifier of this strength gives, not a general figure.
- **Small retry sample.** 55 retries in total, 7 to 17 per model.
- **Real-world applicability.** The harness needs a verifier, and a verifier needs something to check against. It never sees the hidden
  answers (6.3), but the public examples and the kubectl requirements were written by us, after seeing the failures, for tasks whose
  correct output we already knew. In practice the equivalent is whatever checks a user already has: unit tests, a linter or type
  checker, a schema validator, example inputs from the spec, `kubectl --dry-run=server` against a real cluster. Where such a check exists the
  gain (+0.7 to +2.7 questions of 11, x1.3 to x1.95 time) is plausible; where it does not (free text, open-ended questions) the loop
  cannot run, and a verifier weaker than ours will let more wrong answers through (the syntax-only kubectl check let 9 cells through, 6.9).
  The numbers therefore show what a verifier of this strength gives on these tasks, not what any deployment will get.
- **Seeds change sampling only.** All runs use the same prompts; the results say nothing about prompt wording.
- **Machine state.** Retries add latency that grows with the model's size, and the CPU ran at about 90 C (7.5).
- **Grader fix after the fact.** The quoted-flag fix (5.4) was made after seeing the results. It was applied to all saved
  answers at once, changed 3 attempts (Qwen `kubectl-pods-sorted` seeds 43 and 44 on the first attempt, Nemotron seed 43 on
  the second) and no section 5 result. Before the fix Qwen scored 7 / 7 / 7 and Nemotron 8.3 ± 0.6 after one retry.
- **Incident: the laptop suspended.** It went to sleep during the Ornith harness run and resumed about 6.6 hours later. The one
  request in flight recorded 23,880 s. Only the timing was invalid (the answer was valid), so that cell was re-run alone:
  it gave the identical answer in 24.6 s, and the original `conditions.json` was kept for the batch. Later runs were
  protected with `systemd-inhibit` (7.7).

### 6.8 Summary

1. A single run is one draw: three of four models moved by 1 to 1.5 questions (of 11) between seeds, which is as large as
   most differences between models. Ornith's lead over MiMo is the largest gap, but it is not significant (p about 0.2, 6.4).
2. Models fail in different ways: Nemotron repeats the same three mistakes (systematic), Qwen and MiMo change them from
   seed to seed (random), Ornith in between.
3. A generate -> verify -> retry loop with two retries lifted every model to 8.7-10.7 out of 11 and never broke an answer,
   for x1.30 to x1.95 the time. The weakest naked model (MiMo, +2.7) gained most.
4. The verifier's strength was a limit. The syntax-only kubectl check missed all 9 blind-spot cells (missing `-c app`, wrong sort
   field); adding the task requirements (6.9) cut them to 1 and gained Ornith +0.7 and Qwen +0.3 at two retries. It did not help
   Nemotron, which repeats its wrong command after correct feedback.
5. A small model with a harness is competitive on this task set: Qwen 3B with harness (9.3) is a little above Ornith 9B naked (9.0),
   in a similar total time. Qwen2.5-Coder 7B (added last) scored 8.0 on every seed and 10.0 with the harness (6.11), level with MiMo and just below Ornith.
   Size does not predict the score: MiMo 9B (7.3) is below Qwen 3B (7.7), and Qwen 7B equals Nemotron 4B at 8.0.
6. Most of the harness gain is verify-and-resample, not feedback: a control arm that redraws rejected answers with no feedback fixed 25 cells against 26 with feedback (6.5). Only MiMo clearly
   benefited from feedback. The kubectl part of the gain is optimistic (near-oracle verifier); the regex/Python gain is the credible one.
7. The extended run (40 tasks, 5 seeds, 6.13) confirms 6 with statistics: the harness adds 9.5-14.5 pp for every model, feedback adds +0.0 pp [-4.1, +4.8] over plain redraws, and no pairwise gap between models survives Holm correction. Gemma 4 E4B (5.0 GB) ties Ornith 9B (6.12, 6.13).

### 6.9 A stronger kubectl verifier

**Why.** In 6.5 all 9 cells where the verifier accepted an answer the hidden test then failed were kubectl: the offline
parser only checks syntax, so `kubectl logs api-0/app` (valid syntax, wrong meaning) or `--sort-by=createTime` (a legal
flag with a wrong value) passed and the harness never asked for a retry.

**What changed** (`benchmarks/repeat.py`, `kube_parse`, `kube_intent_problems`; requirements in `public.json`):
- After the real-kubectl syntax check, the command is parsed into verb, positional arguments and flags with
  pflag rules (`-n prod`, `-nprod`, `-n=prod`, `--namespace=prod`, `-fc app`, `TYPE/NAME` and `TYPE NAME`, resource aliases
  `po`/`deploy`/`no`, quoted values) and compared with a structured description of the task, taken from the prompt text:
  `logs`: pod `api-0`, container `app`, follow, tail 100; `get pods`: namespace `prod`, sorted by
  `.metadata.creationTimestamp`; `scale`: deployment `web`, namespace `staging`, 5 replicas; `get nodes`: jsonpath
  output that reads `.items` and `.metadata.name`.
- It is still not the hidden grader. The hidden check is a set of regexes on the command text; the verifier
  uses a parsed command and its own requirements, so it accepts spellings and orders the regexes do not
  (see the last bullet) and is stricter on the jsonpath (`{.metadata.name}` alone prints nothing for a node list).
- Feedback states the unmet requirement and what was found, e.g. *"the list is not sorted by the pod creation
  timestamp (sort expression found: 'createTime')"*, *"the container to read should be `app`, the command selects None"*.
  It does not give the corrected command, but for jsonpath it names the two fields the expression must read.
- `KUBECTL_SEMANTIC = False` in `repeat.py` restores the old syntax-only behaviour.

**Validation, no model needed.**
- 34 hand-written commands (14 correct in different spellings, 20 wrong: invented value, wrong pod, wrong
  namespace, `-A`, wrong replica count, missing `-f`, wrong tail, `-o name`, ...): all 34 classified as intended.
- Replay of every saved kubectl answer from all naked and harness runs (`python3 benchmarks/repeat.py --kubectl-replay`,
  47 distinct answers; the first four models alone gave 38, the other 9 come from Qwen 7B, run later), compared with the hidden grade. The table counts *distinct
  answers*, whereas 6.5 counts *cells*: the 9 cells of 6.5 correspond to 8 distinct answers for the first four models, and 10 with the 7B's:

| Verifier | Accepts an answer the hidden test fails | Rejects an answer the hidden test passes |
|---|---:|---:|
| syntax only (used in 6.5) | 10 (`kubectl-logs` 8, `kubectl-pods-sorted` 2); 8 without the 7B | 0 |
| syntax + task requirements | **1** (`kubectl-logs` 1) | 0 |

- The one remaining disagreement is `kubectl logs -f api-0 app --tail=100` (Qwen). The container is given as the
  second positional argument, which kubectl accepts offline and which means the same as `-c app`, but the hidden regex
  requires `-c app`, so the hidden grade is the false negative here. The hidden grader was left unchanged so that the
  scores in sections 5 and 6 stay comparable; re-grading it would turn that one attempt into a pass.

**Re-run with the new verifier.** The 4 kubectl questions were run again in harness mode (4 models x 3 seeds, 48 cells, two retries),
with the other 7 questions left as they were. The old results are kept in `benchmarks/runs/_kubectl_syntax_verifier/`.

- **Same first attempts.** All 48 first attempts are identical to the first run's (same seed, same request), so the
  difference below comes only from the verifier and the retries it triggers. This is a second determinism check.
- **Kubectl passes out of 12 (4 questions x 3 seeds), first attempt, then after two retries:**

| Model | First attempt | Old verifier, +2 retries | New verifier, +2 retries | Answers rejected, old -> new | Verifier OK but hidden failed, old -> new |
|---|---:|---:|---:|---|---|
| Ornith | 10 | 10 | **12** | 0 -> 2 | 2 -> 0 |
| Qwen | 10 | 10 | **11** | 0 -> 1 | 2 -> 1 |
| MiMo | 9 | 11 | 11 | 3 -> 3 | 0 -> 0 |
| Nemotron | 6 | 7 | 7 | 2 -> 6 | 5 -> 0 |

- **3 cells changed from fail to pass**, none the other way: Ornith `kubectl-logs` seeds 42 and 44 (`api-0/app` became
  `pod/api-0 -c app`) and Qwen `kubectl-logs` seed 44 (the retry added the missing `--follow`). By question,
  `kubectl-logs` went from 5/12 to 8/12 after retries; the other three questions did not change.
- **Nemotron: better feedback, same score.** Its first attempts are now rejected 6 times in 12 kubectl cells (before: 2), and the model still returns the same command in half of the
  retries. Five of its 12 kubectl cells remain wrong (`kubectl-logs` 3, `kubectl-pods-sorted` 2).
- **Effect on the whole score** (11 questions, 2 retries): Ornith 10.0 -> 10.7, Qwen 9.0 -> 9.3, MiMo and Nemotron unchanged.
- **Cost.** Retries issued rose from 44 to 55; Ornith's time cost went from x1.25 to x1.30, Nemotron's from x1.29 to x1.50.

The Qwen 7B was run only with this stronger verifier, so it has no before/after comparison here.

**Limits of this check.** The requirements were written by us from the prompts, after seeing the failures; a verifier that
knows the task is close to an oracle for these four prompts, and a real user would need to supply such checks for each task. The
jsonpath requirement (`.items` and `.metadata.name`) is stricter than the hidden regex, which only asks for `metadata.name`.

### 6.10 Sampling settings: what is recommended, and what the benchmark used

All benchmark requests used temperature 0.6, top_p 0.95, top_k 20, no repetition or presence penalty, thinking off, and llama-server's implicit `min_p` 0.05 (found afterwards, see below) (the same for
every model, `PARAMS` in `benchmarks/run.py`). Looked up afterwards:

| Model | Vendor recommendation (model card / `generation_config.json`) | Benchmark setting vs it |
|---|---|---|
| Ornith 1.5 9B | general: temp 1.0, top_p 0.95, top_k 20, min_p 0, presence penalty 1.5; precise coding: temp 0.6, presence penalty 0 | the coding preset |
| MiMo V2.6 Distill Qwen 9B | temp 0.6, top_p 0.95, top_k 20 (`generation_config.json`) | identical |
| Nemotron 3 Nano 4B | temp 1.0, top_p 0.95 for reasoning; temp 0.6, top_p 0.95 for tool calling | tool-calling preset, plus top_k 20 which NVIDIA does not set |
| Qwen2.5-Coder 3B Instruct | temp 0.7, top_p 0.8, top_k 20, repetition penalty 1.05 (`generation_config.json`) | **differs**: temp 0.6 vs 0.7, top_p 0.95 vs 0.8, no repetition penalty (1.05 recommended) |
| Qwen2.5-Coder 7B Instruct | temp 0.7, top_p 0.8, top_k 20, repetition penalty 1.1 (`generation_config.json`) | **differs** in the same way (repetition penalty 1.1) |

So three of four models ran at or near their own recommendation; Qwen2.5-Coder did not, and its scores (notably the loose regexes) may be
slightly affected. (The re-run below tested every model at its vendor setting, and Nemotron at temperature 1.0; no temperature sweep was run.)

General evidence (no source gives one optimum for small models; the vendor setting is the best default):
- Temperature between 0.0 and 1.0 had no statistically significant effect on multiple-choice problem solving across nine LLMs
  ([Renze and Guven, 2024](https://arxiv.org/abs/2402.05201)); this is not a code or exact-match task, so it does not settle our case.
- Min-p beat top-p on general reasoning and creative tasks, mainly at high temperatures ([Nguyen et al., 2024](https://arxiv.org/abs/2407.01082));
  no controlled study of min-p against top-p for small-model code was found.
- Qwen3's card advises against greedy decoding (endless repetition) and suggests a presence penalty of 0-2 against repetition, noting that high
  values can cause language mixing; the Ornith MTP card ([protoLabsAI](https://huggingface.co/protoLabsAI/Ornith-1.5-9B-MTP-GGUF)) measured more looping at low temperature and with llama.cpp defaults
  (greedy 37.5% and defaults 28.1% degenerate generations against 4.7% with the recommended sampler, on its IQ2_M build). Practitioner guides give 0-0.3 for code and extraction, 0.5-0.7 for chat, and
  warn against repetition penalties above about 1.05-1.2 because they distort code
  ([smcleod.net guide](https://smcleod.net/2025/04/llm-sampling-parameters-guide/), [cheat sheet](https://pub.towardsai.net/the-complete-llm-parameters-cheatsheet-2026-5ae47bb14ef3)); these are heuristics, not measurements.
- Gemma 3's team suggests temp 1.0, top_k 64, top_p 0.95, min_p 0 ([Unsloth guide](https://docs.unsloth.ai/basics/tutorial-how-to-run-gemma-3-effectively)),
  an example that the recommended values differ widely between families.

Follow-up still open: a temperature sweep (for example 0.2, 0.6, 1.0, three seeds) on one model. The vendor-setting re-run is below.

**Hidden detail found afterwards: `min_p`.** llama-server's own default is `min_p` 0.05 (read from its `/props`: temperature 0.8, top_k 40, top_p 0.95,
min_p 0.05, repeat_penalty 1.0), and the benchmark never set it. So every earlier run sampled with temperature 0.6, top_p 0.95, top_k 20 **and
min_p 0.05**. The vendor profiles below set every field explicitly (min_p 0, and top_k 0 where the vendor gives none).

**Re-run with the vendor settings** (`make benchmark-vendor`; harness mode, seeds 42/43/44, same questions, same verifier; results in
`benchmarks/runs-vendor/` and `runs-vendor-alt/`, comparison in `runs-vendor/COMPARE.md`). Score out of 11, mean ± SD, per-seed in brackets:

| Model | Vendor settings used | No harness: benchmark -> vendor | After 2 retries: benchmark -> vendor | Speed t/s |
|---|---|---|---|---|
| MiMo 9B | temp 0.6, top_p 0.95, top_k 20, min_p 0 (only `min_p` differs) | 7.3 ± 1.5 -> 7.0 ± 1.0 (8/6/7) | 10.0 ± 1.0 -> 9.3 ± 1.2 (8/10/10) | 3.0 -> 2.8 |
| Nemotron 4B (tool-calling) | temp 0.6, top_p 0.95, top_k off, min_p 0 | 8.0 ± 0.0 -> 8.0 ± 0.0 (8/8/8) | 8.7 ± 0.6 -> 8.7 ± 0.6 (9/9/8) | 5.2 -> 5.0 |
| Nemotron 4B (default config) | temp 1.0, top_p 0.95, top_k off, min_p 0 | 8.0 ± 0.0 -> 6.7 ± 0.6 (6/7/7) | 8.7 ± 0.6 -> 8.3 ± 1.2 (7/9/9) | 5.2 -> 4.7 |
| Qwen2.5-Coder 3B | temp 0.7, top_p 0.8, top_k 20, min_p 0, repetition penalty 1.05 | 7.7 ± 0.6 -> 7.3 ± 0.6 (7/8/7) | 9.3 ± 1.2 -> 8.0 ± 1.7 (7/10/7) | 8.2 -> 8.2 |
| Qwen2.5-Coder 7B | temp 0.7, top_p 0.8, top_k 20, min_p 0, repetition penalty 1.1 | 8.0 ± 0.0 -> 8.3 ± 0.6 (8/8/9) | 10.0 ± 0.0 -> 10.0 ± 0.0 (10/10/10) | 3.4 -> 3.6 |

What it shows:
- **The vendor values did not improve any score materially.** No-harness changes are -0.3 (MiMo), 0.0 (Nemotron), -0.4 (Qwen 3B), +0.3 (Qwen 7B); with two retries -0.7, 0.0, -1.3 and 0.0.
  All of these are within the seed-to-seed SD (up to 1.7), so none is a significant change: 4 of the 8 point down, 3 are zero and the single increase (Qwen 7B +0.3) is one question on one seed (`py-lis`, 0 -> 1 of 3).
- **Nemotron was identical at 0.6.** Removing top_k 20 and min_p 0.05 left every per-question pass count the same (before and after retries); at temperature 1.0 it lost
  1.3 questions without a harness (8.0 -> 6.7, no seed above 7), the one clear effect in this test. Its card recommends 1.0 for reasoning and 0.6
  for tool calling; for these exact-output tasks 0.6 is better.
- **MiMo's only change was `min_p` 0.05 -> 0**, and scores moved by -0.3 / -0.7: dropping the filter did not help, and `min_p` 0.05 may even help small models by
  removing very unlikely tokens, but one seed's difference is a question or two, so this is not shown.
- **Qwen 3B** lost most after retries (9.3 -> 8.0), mainly `kubectl-logs` (2 -> 0 of 3), `regex-hexcolor` (3 -> 1) and `regex-ipv4` (3 -> 2); `py-lis` improved (no harness 0 -> 2 of 3).
  A possible cause is the repetition penalty (1.05) discouraging flags a command needs to repeat, but this was not tested.
- **Qwen 7B** (same vendor values as the 3B, repetition penalty 1.1) was unchanged after retries (10 / 10 / 10 in both cases) and +0.3 without; the 3B's loss did not repeat, which weakens the repetition-penalty explanation above.
- **Conclusion for the benchmark:** the 0.6 / 0.95 / 20 / min_p 0.05 setting used in sections 5-6 is not disadvantaging these models, and the ranking
  and the harness gains do not depend on it within the noise of 3 seeds.

Caveats: each cell is 3 seeds; with a fixed seed but different sampling the random stream differs, so differences of one question are noise; only one
model per family was tested; Ornith was not re-run (its code preset differs from the benchmark only by `min_p`).

### 6.11 Qwen2.5-Coder 7B Instruct (Q4_K_M, 4.7 GB), added last

Added after the other results because it is the same family as the 3B at about 2.5x the size. It was run with exactly the same procedure as the
others: harness mode, seeds 42/43/44, benchmark sampling (temp 0.6, top_p 0.95, top_k 20, implicit min_p 0.05), then again with its vendor
sampling (temp 0.7, top_p 0.8, top_k 20, min_p 0, repetition penalty 1.1). Rows for it are also in 6.4, 6.5 and 6.10; full tables in `benchmarks/runs/STATS.md`.

| | No harness | +1 retry | +2 retries | tok/s | Time cost |
|---|---|---|---|---|---|
| Benchmark sampling | 8.0 ± 0.0 (8/8/8) | 10.0 ± 0.0 | 10.0 ± 0.0 (10/10/10) | 3.4 ± 0.1 | x1.57 |
| Vendor sampling | 8.3 ± 0.6 (8/8/9) | - | 10.0 ± 0.0 (10/10/10) | 3.6 | - |

- **Stable and systematic, like Nemotron.** Score 8, 8, 8; 8 questions always pass, 3 never (`regex-date`, `py-lis`, `py-topk`), none flaky. It is the only model
  with 4/4 on kubectl on every seed (including `kubectl-logs`, which Ornith and the 3B miss), but 2/4 on Python and 2/3 on regexes.
- **The harness fixes most of its failures in one retry.** +2.0 questions (8.0 -> 10.0) on all three seeds, 6 cells fixed, none broken, no verifier-approved answer
  failed the hidden tests. `regex-date` went 0/3 -> 3/3 and `py-lis` 0/3 -> 3/3 after the first retry. `py-topk` stays 0/3: the retries reproduce the
  tie-break bug (the same failure as Ornith's naked `py-topk`, which Ornith does repair).
- **Compared with the others.** Naked, 8.0 is level with Nemotron (8.0) and above the 3B (7.7); with the harness it ties MiMo (10.0) and sits below Ornith (10.7), at
  3.4 t/s against Ornith's 3.9 and the 3B's 8.3. Differences of this size are within the seed noise of the other models (6.4); the point that stands is that its result did not vary at all across seeds.
- **Vendor sampling: no difference.** 8.0 -> 8.3 without harness (only `py-lis` 0 -> 1 of 3) and 10.0 -> 10.0 with it, so the benchmark values were not holding it back.
- **Speed caveat.** 3.4 t/s is below the ~4.3 t/s expected from the 3B's measured ~20 GB/s effective bandwidth (20 / 4.7 GB; the 34 GB/s peak would give 7.2). The machine state recorded for this run shows 2.0 GB of swap in use
  (11.2 GB available) while other work ran on the laptop, so the speed may be understated; the scores are not affected.


### 6.12 Gemma 4 E4B (Q4_K_M, 5.0 GB), added last

Google's Gemma 4 E4B-it (unsloth GGUF). Thinking is off by default (its template adds a thinking token only when `enable_thinking` is true), so the
benchmark flag is a no-op. Run on the 40-task suite (regex 8, Python 12, kubectl 10, SQL 5, shell 5) with the same sampling as the others.
**Reduced protocol, because of time:** the harness stage on 5 seeds (first 2 seeds, then 44-46 so it shares the other models' seeds), but the no-feedback control on seed 42 only. It is included in the pairwise tests and ranks of 6.13; its control row is a single seed.

**MTP investigated, not used.** A drafter GGUF (`mtp-gemma-4-E4B-it-Q8_0.gguf`) loads on our llama.cpp build (`--spec-type draft-mtp --spec-draft-n-max 4`, `-fa off`).
On this CPU (4 threads, 128 greedy tokens, 5 repetitions) plain decoding gave 6.71 ± 0.17 t/s and MTP 6.41 ± 0.02 t/s with only 38% of drafted tokens accepted,
about 5% slower; 8 threads were no better (6.73 vs 6.05). The vendor's 150 -> 214 t/s was measured on a B200 GPU. Accuracy on seed 42 was 34/40 plain and 33/40 with MTP
(`py-editdist` only, sampling noise). Caveat: swap use differed between these runs (1.4 GB to over 6 GB), so the timings are indicative; a clean re-measurement on a quiet machine
is still to do. MTP was therefore not used in the benchmark.

**System prompt (Gemma only).** Without a system prompt Gemma answers in ~112 tokens (up to 480 for Python), against 50-63 for the other models; a 40-task seed took about 12 minutes.
On the 10 longest Python tasks (2 seeds, first attempt, no harness) four system prompts were compared:

| System prompt | Passed | Avg tokens | Avg seconds |
|---|---|---|---|
| none (default) | 18/20 | 326 | 51 |
| "Be concise. Reply with only the final code, regex or command, with no explanation and no comments." | 18/20 | 132 | 22 |
| "Output only a single code block containing the solution. No text before or after it, no comments, no docstrings, no example usage." | 18/20 | 142 | 24 |
| **"You are a terse expert. Give the shortest correct solution as one code block. Never explain, never add tests, comments or usage examples."** (chosen) | 18/20 | 124 | 22 |
| "Answer rules: (1) one code block only, (2) no prose, (3) no comments, (4) prefer a compact idiomatic solution over a long explicit one." | 18/20 | 125 | 22 |

Any of them cuts tokens and time by about 60% with the same pass rate; the wording does not matter. The chosen prompt was applied to Gemma only, so Gemma's run differs from the others in this one condition
(`gemma-4-e4b-terse` in `models.json`; an earlier trial with the first prompt on all 40 tasks, seed 42, gave 112 -> 68 tokens per answer and 34/40 first attempt either way).

**Results (terse prompt, 40 tasks, harness on 5 seeds).** After the first two seeds the harness stage was extended to seeds 44-46 so Gemma could be compared with the others on the same seeds;
its control arm (no feedback) was run on seed 42 only.

| | seed 42 | 43 | 44 | 45 | 46 | mean ± SD |
|---|---|---|---|---|---|---|
| First attempt | 35 | 32 | 33 | 32 | 33 | **33.0 ± 1.2** (82.5%) |
| + 2 retries with feedback (harness) | 38 | 39 | 39 | 39 | 39 | **38.8 ± 0.4** (97.0%) |
| Control: redraw without feedback | 35 | - | - | - | - | - |

- Per type, first attempt (mean of 5 seeds): regex 6.8/8, Python 11.0/12, kubectl 8.2/10, SQL 4.0/5, shell 3.0/5.
- Failed on the first try on every seed: `py-flatten`, `kubectl-exec`, `sql-second-salary`, `sh-count-errors`, `sh-top-ips`. After retries only `sh-count-errors` (0 of 5) and `sh-top-ips` (4 of 5) still fail.
- **On the original 11 tasks** (directly comparable with 6.4/6.5): first attempt 10.0 ± 0.7 of 11 (11, 9, 10, 10, 10), with 2 retries 11.0 ± 0.0.
- **Versus Ornith** (same seeds): +1.0 pp on the first attempt, 95% paired-bootstrap CI [-8.5, +10.5], p = 0.92 - a tie. Gemma is ahead of Qwen 3B (+12.5 pp, raw p = 0.025, Holm 0.25) and level with Qwen 7B (+4.5 pp, p = 0.55).
  Its advantages are speed and size, not accuracy: x1.20 time cost against Ornith's x1.37, 5.0 GB against 5.8 GB, and 6.7 against 3.9 t/s generation.
- Feedback on seed 42: the control fixed 0 of the 5 first-attempt failures while the harness fixed 3. One seed only; the five-seed control was not run (time).
- Caveats: Gemma is the only model that had a system prompt; the control arm has 1 seed; speed was measured while the machine was swapping (a clean repeat is still to do).

### 6.13 Extended benchmark: 40 tasks, 5 seeds, control arm

Run with `benchmarks/run_extended.sh` (harness stage, then the no-feedback control) and analysed with `benchmarks/analysis.py` (full tables in `benchmarks/ANALYSIS.md`, `benchmarks/runs/RESAMPLE.md`).
Models: Qwen 3B, Nemotron 4B, Qwen 7B and Ornith 9B (200 graded cells for each of the harness and control stages); Gemma 4 E4B (harness 200 cells, control 40, 6.12).
**MiMo 9B was excluded**: it needs about twice the time per task (3.1 tok/s, long answers and retries); it was stopped at 101 of 200 harness cells and 33 control cells and its original 11-task, 3-seed results (6.4-6.5) are all that is reported.
The first attempt of each harness cell is the "no harness" score (same seed as a naked run). Statistics treat the **questions as the sample** (bootstrap over questions); seeds only add sampling noise.
The hidden `kubectl-logs` check was fixed before this run (it now accepts the positional form `logs api-0 app`), and saved answers were re-graded; Qwen 3B's 11-task, 3-seed numbers moved accordingly: first attempt 7.7 ± 0.6 -> 8.0 ± 1.0, with 2 retries 9.3 ± 1.2 -> 9.7 ± 0.6, control 10.3 ± 0.6. The tables in 6.4, 6.5 and 6.10 and items 5 of 6.8 and 5 of section 8 still show the pre-fix values for Qwen 3B (the other models did not change).

**Score out of 40 (mean ± SD over 5 seeds); pass rate with 95% CI.**

| Model | First attempt /40 | pass % [95% CI] | + 2 retries /40 | pass % [95% CI] | control /40 | time cost H / R |
|---|---|---|---|---|---|---|
| Gemma 4 E4B (terse prompt) | 33.0 ± 1.2 | 82.5 [70.5, 93.0] | 38.8 ± 0.4 | 97.0 [91.5, 100.0] | (1 seed: 35) | x1.20 / - |
| Ornith 1.5 9B + MTP | 32.6 ± 1.9 | 81.5 [71.5, 90.5] | 38.2 ± 1.3 | 95.5 [90.5, 99.0] | 37.6 ± 0.9 | x1.37 / x1.24 |
| Qwen2.5-Coder 7B | 31.2 ± 1.8 | 78.0 [66.0, 88.5] | 35.0 ± 0.7 | 87.5 [78.0, 95.5] | 34.8 ± 1.3 | x1.40 / x1.39 |
| Qwen2.5-Coder 3B | 28.0 ± 1.9 | 70.0 [58.5, 81.0] | 32.4 ± 1.5 | 81.0 [71.0, 90.0] | 33.4 ± 1.7 | x1.52 / x1.40 |
| Nemotron 3 Nano 4B | 27.6 ± 1.8 | 69.0 [56.5, 80.5] | 32.0 ± 1.2 | 80.0 [69.0, 89.5] | 31.8 ± 0.8 | x1.50 / x1.31 |

**By task type, first attempt (mean ± SD of the per-seed score):**

| Model | regex /8 | Python /12 | kubectl /10 | SQL /5 | shell /5 |
|---|---|---|---|---|---|
| Gemma 4 E4B | 6.8 ± 0.8 | 11.0 ± 0.0 | 8.2 ± 0.4 | 4.0 ± 0.0 | 3.0 ± 0.0 |
| Ornith 9B + MTP | 7.0 ± 0.7 | 9.4 ± 1.5 | 8.4 ± 0.5 | 4.2 ± 0.8 | 3.6 ± 0.5 |
| Qwen 7B | 5.2 ± 0.4 | 9.0 ± 0.7 | 8.8 ± 0.4 | 4.6 ± 0.5 | 3.6 ± 0.9 |
| Qwen 3B | 4.8 ± 1.6 | 9.4 ± 0.5 | 7.6 ± 0.9 | 4.4 ± 0.9 | 1.8 ± 1.1 |
| Nemotron 4B | 4.6 ± 0.9 | 10.4 ± 0.5 | 5.6 ± 1.1 | 4.6 ± 0.5 | 2.4 ± 0.9 |

- **Two tiers, no strict ranking.** Gemma, Ornith and Qwen 7B (78-83%) lead Qwen 3B and Nemotron (69-70%). Of the 10 pairwise differences none survives Holm correction (smallest raw p = 0.025 for Gemma vs Qwen 3B, Holm 0.25); rank stability: P(best) Gemma 50%, Ornith 34%, Qwen 7B 16%.
  Seed-to-seed SD is 1.2-1.9 questions, but the question sample dominates (every 95% CI is about ±10 pp).
- **Different failure profiles.** Nemotron is best at Python (10.4/12) and worst at kubectl (5.6/10); Qwen 3B collapses on shell (1.8/5); shell is the hardest type for all (57.6% mean pass rate), SQL the easiest (87.2%).
  Never passed on the first attempt on any seed: Ornith 1 task, Gemma 5, Qwen 7B 5, Qwen 3B 6, Nemotron 7. No question is failed by every model; 11 of 40 are passed by every model on every seed.
- **Harness gain (H - N), pass-rate points, paired over questions:** Gemma +14.5 [+5.0, +25.0], Ornith +14.0 [+6.5, +23.0], Nemotron +11.0 [+5.5, +18.0], Qwen 3B +11.0 [+5.5, +18.0], Qwen 7B +9.5 [+3.0, +17.5]; all Holm p <= 0.016. No cell broke with feedback; two broke in the control.
- **Mostly resampling, not feedback.** Pooled over the four models with a control arm, H - N = +12.0 pp [+7.4, +17.2], R - N = +11.4 pp [+7.7, +15.4], and the feedback itself (H - R) adds +0.0 pp [-4.1, +4.8] (p = 1.0).
  Of 203 first-attempt failures, feedback fixed 91 and plain redraws 93 (McNemar on the discordant cells, p = 0.91). By type: regex+Python 58 (feedback) vs 75 (redraw), kubectl 33 vs 18 - feedback helps command tasks, redraws help regex and code.
- **Verifier quality.** Over 1000 first attempts the public verifier agreed with the hidden test on all but 23: 15 false accepts (6.3% of hidden failures) and 8 false rejects (1.0% of passes). The false accepts are concentrated in shell (12 of 53 hidden failures, 22.6%) and Python (3 of 54);
  regex, SQL and kubectl had none. The shell verifier is the weakest because its public fixture exercises fewer edge cases than the hidden one.
- **Variance.** Between-question variance (stable difficulty) is 0.09-0.15 per cell against 0.02-0.08 within-question (sampling): which questions a model fails matters more than the seed. Flaky questions (outcome changes with the seed): Gemma 4, Qwen 7B 9, Nemotron 12, Ornith 13, Qwen 3B 16.
- **Cost.** Tokens per first attempt: Qwen 7B 50, Nemotron 56, Gemma 58 (with the terse prompt), Ornith 58, Qwen 3B 63; the harness costs x1.2-x1.5 the time of a single attempt, the control x1.24-x1.40. Wall-clock speed including prompt processing: Qwen 3B 8.9, Nemotron 5.5, Gemma 4.7, Ornith 4.2, Qwen 7B 3.8 tok/s.

## 7. Server optimisation: getting the most out of the test machine

How the server and the test setup were tuned for this laptop, what was measured to matter, what
made no difference, and what was not tried. Numbers marked *(s4)* are steady-state figures from
section 4 (Qwen2.5-Coder-3B and Ornith 9B); the machine state in 7.5 was read during the section 6 runs.

### 7.1 The limit: memory bandwidth, not compute

Generating a token reads every weight once, so `tokens/s <= bandwidth / model size`. With the measured
34 GB/s peak (the effective figure reached in practice is about 20 GB/s, so the second figure in the ceiling column is the realistic one):

| Model (Q4_K_M) | File | Bandwidth ceiling | Best measured *(s4)* | Comment |
|---|---:|---:|---:|---|
| Qwen2.5-Coder 3B | 1.9 GB | ~18 t/s at peak (~10.7 at the 20 GB/s measured) | 10.7 t/s (~20 GB/s effective) | saturated, flags do not move it |
| Nemotron 3 Nano 4B | 2.8 GB | ~12 t/s at peak (~7 at 20 GB/s) | 5-6 t/s | about 70-85% of the ~7 t/s ceiling at 20 GB/s effective; a kernel limit is possible but not shown |
| Ornith / MiMo 9B | 5.8 GB | ~6 t/s at peak (~3.4 at 20 GB/s) | Ornith 3.7 t/s plain, 4.7 t/s with MTP; MiMo 3.2-3.5 t/s | MTP gets more than one token per weight read |

Consequences: model size is the biggest lever; the iGPU shares the same RAM bus and adds no bandwidth;
and anything else that touches memory (a second server, a browser, swapping) takes bandwidth from the benchmark.

### 7.2 What helped (measured)

| Change | Effect |
|---|---|
| Smaller, quantised model (Q4_K_M) | ceiling scales with 1/size; the 3B model is 2-3x faster than the 9B models |
| 4 threads (= physical cores) instead of 8 | 10.7 vs 8.7 t/s: hyperthreads compete for bandwidth. 3 and 6 threads: 10.5 each |
| MTP speculative decoding, draft length 1-2 | Ornith 3.7 -> **4.7 t/s (+27%)**, same memory; default draft length gave only 3.9 t/s |
| CPU instead of the Vulkan iGPU for generation | 10.7 vs 6.2-6.7 t/s; the iGPU only matches the CPU at prefill |
| Free RAM, no swap | with swap nearly full the 9B runs were depressed; section 6 runs started with ~13 GB available and empty swap |
| Thinking off | at ~4.7 t/s a reasoning trace costs minutes; a trace-free answer takes about 6-30 s (section 5.1) |

### 7.3 What made no measurable difference

Flash attention, a q8 KV cache, `--no-mmap`, a larger batch (`-b 2048`): all stayed at 10.7 t/s *(s4)*.
A 0.5B draft model from another family was **worse** (7.4 t/s, 43% acceptance); n-gram speculation gave
11.1 t/s, about +4% and dependent on the content.

### 7.4 Server and test configuration, and why

| Setting | Value | Reason |
|---|---|---|
| Backend | LM Studio's bundled llama.cpp (Vulkan build) run CPU-only: `-ngl 0 -t 4` | the iGPU path is slower for generation; 4 threads as above |
| Context | 4k for benchmarks, 16k for interactive chat | smaller KV cache, less memory traffic; the benchmark prompts and answers fit |
| One `llama-server` per model | started once, reused for all seeds and questions | model load happens once, so timings measure generation only |
| Strictly one model at a time | batches run sequentially, nothing else heavy during runs | two servers (or a build or PDF export) would split the same 34 GB/s and the same RAM |
| `cache_prompt: false` in the repeated runs | every request starts from scratch | repeated identical prompts would otherwise reuse the prompt prefix and look faster |
| Fixed sampling, per-run seed | temp 0.6, top_p 0.95, top_k 20, `max_tokens` 512 | comparable runs; the seed is the only thing that varies |
| `enable_thinking=false` | on every request | see 7.2 |
| Health wait, then `terminate` per model | up to 6 min for startup | a model that fails to load stops the batch instead of recording garbage |
| Conditions logged | `runs/<mode>/<model>/conditions.json`: time, uptime, free RAM, swap used, load | runs can be compared honestly later |

### 7.5 Machine state during the runs

Read from sysfs at 22:08 while the batch was running (not changed by us):

| Item | Value |
|---|---|
| Power | AC connected, battery 98% charging |
| CPU governor | `intel_pstate`, `powersave` (the driver default), energy preference `balance_performance` |
| Turbo | enabled (`no_turbo=0`), max 4.7 GHz; the busy cores ran at about 3.8 GHz |
| Threads | 4 cores / 8 threads (SMT on); 4 used by the server |
| Temperatures | package **91 C**, hottest sensor 90 C under the 4-thread load |
| Free RAM at batch start | ~9 GB free (13 GB available), swap empty |

The package is at about 91 C and the clocks sit below the 4.7 GHz maximum, so thermal limits probably
cap sustained speed on this ultrabook. Generation is bandwidth-bound and less sensitive to clocks than
prefill, but run-to-run variation and prefill timings can be affected. This was observed, not measured
as a cause.

### 7.6 Not tried: possible further headroom

These are untested ideas, not findings.

- **Cooling and power:** a stand or a cooler room, and the `performance` energy preference, then check whether
  the clock stays at 3.8 GHz or higher over a long run and whether prefill speed rises.
- **Build for this CPU:** it supports AVX-512 (including VNNI), but all backends bundled with LM Studio are
  AVX2 builds. A native llama.cpp build could speed up prefill (compute-bound); generation (bandwidth-bound)
  probably would not change. The bundled CPU-only AVX2 backend was not compared with the Vulkan build run at `-ngl 0`.
- **Smaller quantisations:** Ornith `IQ4_XS` (5.45 GB) or `IQ3_M` (4.67 GB) raise the bandwidth ceiling (the model card warns
  that `IQ3_M` needs the recommended sampler and `IQ2_M` degenerates).
- **Memory:** confirm the RAM runs in dual-channel mode (`dmidecode` needs root, so it was not checked) and that
  nothing else competes for it.
- **Thread pinning** (`taskset` to one thread per core) was not tried.

### 7.7 Checklist before a benchmark run

1. Reboot, or make sure swap is empty and free RAM is at least the model size plus 2 GB.
2. AC power connected; keep the laptop ventilated; note the temperature.
3. **Block suspend and idle** for the length of the run, e.g.
   `systemd-inhibit --what=sleep:idle --who=benchmark --why=run sleep 7200 &`. The laptop slept in the middle of the
   section 6 batch and one request recorded 23,880 s (6.7).
4. Close everything else (browser, builds, PDF exports); never run two servers at once.
5. `make stop-all`, then confirm port 8080 (chat server) and port 8089 (the benchmark scripts start their own `llama-server` there) are free.
6. One model at a time, `-ngl 0 -t 4`, thinking off, fixed sampling, `cache_prompt` off.
7. Record the conditions (done automatically in `conditions.json`) and keep comparisons within one session.
8. After the run, scan for impossible timings (a request far longer than any other) before trusting speed figures.

## 8. Recommendations

1. **Interactive chat**: use a 3-4B model at Q4_K_M. A 3B Qwen model gives ~10 t/s, Nemotron 3 Nano 4B ~6 t/s; a 9B model
   gives 4-5 t/s at best on this machine.
2. **9B-class models**: prefer builds with MTP (Ornith MTP), run on CPU with 4 threads and
   `--spec-draft-n-max 2`. Close other applications first; free RAM is the second constraint.
3. **Keep thinking off** for chat. At ~4.7 t/s a reasoning trace costs minutes; use a
   budget (128-512) when reasoning is worth the wait.
4. **Don't bother with** extra llama.cpp flags, more threads, the Vulkan GPU path, or a
   small draft model from a different family. None helped here.
5. **Task quality**: quote means over several seeds, not single runs. On the 40-task suite (6.13, 5 seeds) the first-attempt scores are Gemma 4 E4B 33.0 ± 1.2, Ornith 32.6 ± 1.9, Qwen 7B 31.2 ± 1.8, Qwen 3B 28.0 ± 1.9 and Nemotron 27.6 ± 1.8 out of 40, and the top three are statistically tied. On the original 11 tasks, without a harness, Ornith scored 9.0 ± 1.0 out of 11,
   Nemotron 8.0 ± 0.0, Qwen2.5-Coder 7B 8.0 ± 0.0, Qwen2.5-Coder 3B 7.7 ± 0.6 and MiMo 7.3 ± 1.5 (section 6.4); the single run of section 5 overstated
   MiMo and understated Qwen's regexes. Ornith's lead over MiMo is not statistically significant with three seeds (6.4). Nemotron 4B remains the best speed/quality
   trade-off for quick snippet questions, but its three failures (`regex-date`, the `kubectl` sort and logs commands) repeat on
   every seed.
6. **Add a verify -> retry loop for code, regex and command tasks.** With two retries it lifted every model to 8.7-10.7 out of
   11 and broke nothing, for x1.30-x1.95 the time (section 6.5); Qwen2.5-Coder 7B went 8.0 -> 10.0 on every seed (6.11). Use executable checks: examples for regexes, assertions
   and a timing check for functions, the real CLI parser for commands. It helps even Ornith (+1.7), contrary to the earlier
   assumption, though a no-feedback redraw gave almost the same gain (6.5): the value is mainly in having a check that detects a wrong answer. A syntax-only command check misses semantic mistakes (a missing `-c app`); checking the required flags and values (6.9) removed
   8 of 9 such misses and gained +0.7 for Ornith, but not for Nemotron, which repeats its wrong command.
7. **Possible next steps** (the positional-container `kubectl-logs` fix and the 40-task, 5-seed run are done, 6.13): the Gemma control arm on 5 seeds, a clean throughput re-measurement (Gemma with and without MTP), more questions to separate the top three models; Ornith `IQ4_XS` (5.45 GB) or `IQ3_M` (4.67 GB) for more speed
   (the model card warns `IQ3_M` needs the recommended sampler and `IQ2_M` degenerates); a thinking-on comparison on
   reasoning problems; the hardware ideas in 7.6.
