# ornith-9b-mtp / kubectl-pods-sorted

- category: kubectl
- result: **PASS** (all parts present)
- tokens: 19 in 7s (2.6 t/s), finish: stop

## Prompt

Give the single kubectl command to list all pods in the namespace `prod`, sorted by creation timestamp. Reply with ONLY the command in a code block.

## Answer

```bash
kubectl get pods -n prod --sort-by=.metadata.creationTimestamp
```
