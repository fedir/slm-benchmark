# nemotron-3-nano-4b / kubectl-top / seed 46 / harness

## Prompt

Give the single kubectl command to show the CPU and memory usage of the pods in namespace `prod`, sorted by memory. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 19 tokens in 4.5s, finish: stop
- verifier: pass

```bash
kubectl top pods --namespace=prod --sort-by=memory
```
