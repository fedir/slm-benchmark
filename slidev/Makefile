.PHONY: run build pdf

# host has no node; slides live inside the "tools" distrobox container
IN_CONTAINER := $(shell [ -n "$$CONTAINER_ID" ] && echo 1)
ifeq ($(IN_CONTAINER),1)
RUN :=
else
RUN := distrobox-enter -n tools --
endif

# Node here resolves "localhost" to ::1 only, so the dev server was
# unreachable at http://127.0.0.1:PORT even though ::1/localhost worked.
# Forcing IPv4-first DNS order makes it bind 127.0.0.1 too.
run:
	$(RUN) env NODE_OPTIONS=--dns-result-order=ipv4first npm run dev

build:
	$(RUN) npm run build

pdf:
	$(RUN) npm run export -- --output slides.pdf --per-slide
