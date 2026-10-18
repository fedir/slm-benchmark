# qwen2.5-coder-7b / kubectl-pods-sorted / seed 43 / harness

## Prompt

Give the single kubectl command to list all pods in the namespace `prod`, sorted by creation timestamp. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 19 tokens in 6.2s, finish: stop
- verifier: pass

```sh
kubectl get pods -n prod --sort-by=.metadata.creationTimestamp
```
