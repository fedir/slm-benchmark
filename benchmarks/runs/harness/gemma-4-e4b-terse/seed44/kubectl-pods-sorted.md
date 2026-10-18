# gemma-4-e4b-terse / kubectl-pods-sorted / seed 44 / harness

## Prompt

Give the single kubectl command to list all pods in the namespace `prod`, sorted by creation timestamp. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 21 tokens in 6.5s, finish: stop
- verifier: pass

```bash
kubectl get pods -n prod --sort-by=.metadata.creationTimestamp
```
