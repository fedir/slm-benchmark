#!/bin/bash
# Extended suite: 40 tasks x seeds 42-46. Harness (retry with feedback) first, then the no-feedback control arm.
# MiMo-9B is excluded from the extended run: too slow (see REPORT.md / paper); its 3-seed, 11-task results remain.
cd "$(dirname "$0")/.."
SEEDS=42,43,44,45,46
MODELS="qwen2.5-coder-3b nemotron-3-nano-4b qwen2.5-coder-7b ornith-9b-mtp gemma-4-e4b-terse"
for m in $MODELS; do python3 benchmarks/repeat.py --mode harness -m $m --seeds $SEEDS; done
echo HARNESS-DONE
for m in $MODELS; do python3 benchmarks/repeat.py --mode resample -m $m --seeds $SEEDS; done
echo ALL-DONE
