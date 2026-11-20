.PHONY: benchmark-extended benchmark-analysis benchmark-speed validate-tasks paper benchmark-vendor benchmark-compare benchmark benchmark-summary benchmark-repeat benchmark-stats run-ornith run-mimo run-nemotron stop-all stop dev-slides build-slides export-slides help

# Machine-specific paths (git-ignored); see local.conf.sample
-include local.conf
MODELS_DIR ?= $(HOME)/.lmstudio/models

help:
	@echo "make run-ornith   start Ornith 9B MTP server on :8080 (foreground, Ctrl+C to stop)"
	@echo "make run-mimo     start MiMo V2.6 Distill Qwen 9B server on :8080"
	@echo "make run-nemotron start Nemotron 3 Nano 4B server on :8080"
	@echo "make benchmark    run all models x all questions (MODELS=a,b to limit, FORCE=1 to redo)"
	@echo "make benchmark-summary  rebuild benchmarks/results/SUMMARY.md"
	@echo "make benchmark-repeat   3 seeds per question; MODE=naked|harness MODELS=a,b (see benchmarks/repeat.py)"
	@echo "make benchmark-vendor  re-run mimo, nemotron, qwen with vendor-recommended sampling and compare"
	@echo "make benchmark-compare  compare runs-vendor/ with the default runs"
	@echo "make benchmark-stats    rebuild benchmarks/runs/STATS.md"
	@echo "make benchmark-extended 40 tasks x 5 seeds: harness then no-feedback control, all models (hours; see benchmarks/run_extended.sh)"
	@echo "make benchmark-analysis statistics (CIs, paired tests) -> benchmarks/ANALYSIS.md"
	@echo "make benchmark-speed   throughput experiment with repetitions (quiet machine)"
	@echo "make validate-tasks    check every extended-suite grader against known-good/bad answers"
	@echo "make paper             regenerate tables/figures and build paper/main.pdf"
	@echo "make stop-all     stop every running llama-server"
	@echo "make dev-slides    slidev dev server on :3030 (slidev/, foreground)"
	@echo "make build-slides  static-build the deck (slidev/dist/)"
	@echo "make export-slides export the deck to slidev/slides.pdf"

run-ornith:
	./serve.sh

run-mimo:
	MODEL=$(MODELS_DIR)/bartowski/MiMo-V2.6-Distill-Qwen-9B-GGUF/MiMo-V2.6-Distill-Qwen-9B-Q4_K_M.gguf SPEC= ./serve.sh

run-nemotron:
	MODEL=$(MODELS_DIR)/lmstudio-community/NVIDIA-Nemotron-3-Nano-4B-GGUF/NVIDIA-Nemotron-3-Nano-4B-Q4_K_M.gguf SPEC= ./serve.sh

stop-all stop:
	@pkill -x llama-server && echo "llama-server stopped" || echo "no llama-server running"

benchmark:
	python3 benchmarks/run.py $(if $(MODELS),-m $(MODELS)) $(if $(QUESTIONS),-q $(QUESTIONS)) $(if $(FORCE),--force)

benchmark-summary:
	python3 benchmarks/run.py --summary

# Sampling: SAMPLING=vendor uses each model's recommended values from benchmarks/models.json ("sampling"); results go to
# benchmarks/runs-<profile>/. Explicit values (TEMP, TOP_P, TOP_K, MIN_P, REPEAT_PENALTY, PRESENCE_PENALTY) override and need TAG=name.
benchmark-repeat:
	python3 benchmarks/repeat.py --mode $(or $(MODE),naked) $(if $(MODELS),-m $(MODELS)) $(if $(SEEDS),--seeds $(SEEDS)) $(if $(FORCE),--force) \
		$(if $(SAMPLING),--sampling $(SAMPLING)) $(if $(TAG),--tag $(TAG)) $(if $(TEMP),--temperature $(TEMP)) $(if $(TOP_P),--top-p $(TOP_P)) \
		$(if $(TOP_K),--top-k $(TOP_K)) $(if $(MIN_P),--min-p $(MIN_P)) $(if $(REPEAT_PENALTY),--repeat-penalty $(REPEAT_PENALTY)) \
		$(if $(PRESENCE_PENALTY),--presence-penalty $(PRESENCE_PENALTY))

# Re-run MiMo, Nemotron and Qwen (harness mode, 3 seeds) with the vendor-recommended sampling, then compare with the default runs.
benchmark-vendor:
	python3 benchmarks/repeat.py --mode harness -m qwen2.5-coder-3b,nemotron-3-nano-4b,mimo-9b --sampling vendor
	python3 benchmarks/repeat.py --mode harness -m nemotron-3-nano-4b --sampling vendor-alt
	$(MAKE) benchmark-compare

benchmark-compare:
	python3 benchmarks/repeat.py --compare vendor
	-python3 benchmarks/repeat.py --compare vendor-alt

benchmark-stats:
	python3 benchmarks/repeat.py --stats

dev-slides:
	$(MAKE) -C slidev run

build-slides:
	$(MAKE) -C slidev build

export-slides:
	$(MAKE) -C slidev pdf

# Extended suite: 40 tasks, seeds 42-46; harness (retry with feedback) then the no-feedback control arm. Takes many hours; run under systemd-inhibit.
benchmark-extended:
	systemd-inhibit --what=sleep:idle --who=benchmark --why=extended benchmarks/run_extended.sh

benchmark-analysis:
	python3 benchmarks/analysis.py

benchmark-speed:
	python3 benchmarks/speed.py

validate-tasks:
	python3 benchmarks/tasks_v2.py --check

paper:
	python3 benchmarks/analysis.py
	python3 paper/make_tables.py
	distrobox-enter -n tools -- python3 paper/make_figs.py
	distrobox-enter -n tools -- bash -c "cd paper && latexmk -pdf -interaction=nonstopmode main.tex"
