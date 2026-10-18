# nemotron-3-nano-4b / kubectl-pods-sorted / seed 42 / harness

## Prompt

Give the single kubectl command to list all pods in the namespace `prod`, sorted by creation timestamp. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 24 tokens in 6.4s, finish: stop
- verifier: pass

```bash
kubectl get pods -n prod -o wide --sort-by=.metadata.creationTimestamp
```
