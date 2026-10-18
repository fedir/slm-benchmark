# nemotron-3-nano-4b / kubectl-top / seed 43 / resample (no feedback)

## Prompt

Give the single kubectl command to show the CPU and memory usage of the pods in namespace `prod`, sorted by memory. Reply with ONLY the command in a code block.

## Attempt 1: FAIL (hidden: missing ['--sort-by[ =]memory\\b'])

- 20 tokens in 4.9s, finish: stop
- verifier: FAIL: kubectl rejected the command: error: --sort-by accepts only cpu or memory

```bash
kubectl top pods -n prod --sort-by=.memory.usage
```

## Attempt 2: FAIL (hidden: missing ['--sort-by[ =]memory\\b'])

- 22 tokens in 5.1s, finish: stop
- verifier: FAIL: it must be a single kubectl invocation: no pipes, redirects or substitutions

```bash
kubectl top pods -n prod | sort -k "Memory" -n
```

## Attempt 3: PASS (hidden: all parts present)

- 19 tokens in 4.5s, finish: stop
- verifier: pass

```bash
kubectl top pods --namespace=prod --sort-by=memory
```
