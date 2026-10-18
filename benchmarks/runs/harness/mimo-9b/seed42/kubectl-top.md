# mimo-9b / kubectl-top / seed 42 / harness

## Prompt

Give the single kubectl command to show the CPU and memory usage of the pods in namespace `prod`, sorted by memory. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 19 tokens in 7.4s, finish: stop
- verifier: FAIL: kubectl rejected the command: error: --sort-by accepts only cpu or memory

```bash
kubectl top pods -n prod --sort-by='memory-used'
```

## Attempt 2: PASS (hidden: all parts present)

- 17 tokens in 9.6s, finish: stop
- verifier: pass

```bash
kubectl top pods -n prod --sort-by=memory
```
