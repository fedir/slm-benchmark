# ornith-9b-mtp / kubectl-pods-sorted / seed 44 / resample (no feedback)

## Prompt

Give the single kubectl command to list all pods in the namespace `prod`, sorted by creation timestamp. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 19 tokens in 6.0s, finish: stop
- verifier: pass

```bash
kubectl get pods -n prod --sort-by=.metadata.creationTimestamp
```
