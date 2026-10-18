# gemma-4-e4b / kubectl-pods-sorted / seed 42 / naked

## Prompt

Give the single kubectl command to list all pods in the namespace `prod`, sorted by creation timestamp. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 21 tokens in 5.0s, finish: stop

```bash
kubectl get pods -n prod --sort-by=.metadata.creationTimestamp
```
