# ornith-9b-mtp / kubectl-pods-sorted / seed 46 / harness

## Prompt

Give the single kubectl command to list all pods in the namespace `prod`, sorted by creation timestamp. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 18 tokens in 5.7s, finish: stop
- verifier: pass

```
kubectl get pods -n prod --sort-by=.metadata.creationTimestamp
```
