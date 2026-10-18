# qwen2.5-coder-3b / kubectl-pods-sorted / seed 45 / harness

## Prompt

Give the single kubectl command to list all pods in the namespace `prod`, sorted by creation timestamp. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 19 tokens in 2.8s, finish: stop
- verifier: pass

```bash
kubectl get pods -n prod --sort-by='.metadata.creationTimestamp'
```
