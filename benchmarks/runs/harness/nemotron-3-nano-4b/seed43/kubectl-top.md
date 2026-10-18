# nemotron-3-nano-4b / kubectl-top / seed 43 / harness

## Prompt

Give the single kubectl command to show the CPU and memory usage of the pods in namespace `prod`, sorted by memory. Reply with ONLY the command in a code block.

## Attempt 1: FAIL (hidden: missing ['--sort-by[ =]memory\\b'])

- 20 tokens in 4.9s, finish: stop
- verifier: FAIL: kubectl rejected the command: error: --sort-by accepts only cpu or memory

```bash
kubectl top pods -n prod --sort-by=.memory.usage
```

## Attempt 2: PASS (hidden: all parts present)

- 18 tokens in 6.3s, finish: stop
- verifier: pass

```bash
kubectl top pods -n prod --sort-by=memory
```
