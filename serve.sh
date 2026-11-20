#!/bin/bash
# Launch llama-server (LM Studio's Vulkan build) (default: Ornith 1.5 9B MTP), CPU only.
# Usage: ./serve.sh [extra llama-server args]   e.g. ./serve.sh -c 8192 --port 8081
set -e

HERE=$(cd "$(dirname "$0")" && pwd)
[ -f "$HERE/local.conf" ] && . "$HERE/local.conf"   # MODELS_DIR, BACKEND_DIR (see local.conf.sample)
MODELS_DIR=${MODELS_DIR:-$HOME/.lmstudio/models}
BACKEND_DIR=${BACKEND_DIR:-/var/lib/flatpak/app/ai.lmstudio.lm-studio/x86_64/stable/active/files/extra/lmstudio/resources/app/.webpack/bin/extensions/backends/llama.cpp-linux-x86_64-vulkan-avx2-*}
BACKEND=${BACKEND:-$(ls -d $BACKEND_DIR | sort -V | tail -1)}
if [ ! -x "$BACKEND/llama-server" ]; then echo "llama-server not found: copy local.conf.sample to local.conf and set BACKEND_DIR" >&2; exit 1; fi
# Override per model, e.g. MODEL=... SPEC="" ./serve.sh   (SPEC empty = no speculative decoding)
MODEL=${MODEL:-$MODELS_DIR/protoLabsAI/Ornith-1.5-9B-MTP-GGUF/Ornith-1.5-9B-MTP-Q4_K_M.gguf}
SPEC=${SPEC---spec-type draft-mtp --spec-draft-n-max 2}
PORT=8080

if curl -s "localhost:$PORT/health" >/dev/null 2>&1; then
  echo "A server is already running on port $PORT." >&2
  exit 1
fi

export LD_LIBRARY_PATH=$BACKEND
echo "Serving on http://localhost:$PORT  (open chat.html to chat)"
exec "$BACKEND/llama-server" \
  -m "$MODEL" \
  -ngl 0 -t 4 \
  $SPEC \
  -c 16384 --port "$PORT" \
  "$@"
