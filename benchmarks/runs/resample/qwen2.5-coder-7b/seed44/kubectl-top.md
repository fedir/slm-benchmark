# qwen2.5-coder-7b / kubectl-top / seed 44 / resample (no feedback)

## Prompt

Give the single kubectl command to show the CPU and memory usage of the pods in namespace `prod`, sorted by memory. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 17 tokens in 5.3s, finish: stop
- verifier: pass

```sh
kubectl top pods --namespace prod --sort-by=memory
```
