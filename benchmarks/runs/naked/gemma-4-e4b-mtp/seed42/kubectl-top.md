# gemma-4-e4b-mtp / kubectl-top / seed 42 / naked

## Prompt

Give the single kubectl command to show the CPU and memory usage of the pods in namespace `prod`, sorted by memory. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 18 tokens in 4.8s, finish: stop

```bash
kubectl top pods -n prod --sort-by=memory
```
