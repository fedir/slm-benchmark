# mimo-9b / kubectl-pods-sorted

- category: kubectl
- result: **FAIL** (missing ['--sort-by[ =]\\.?metadata\\.creationTimestamp'])
- tokens: 18 in 8s (2.4 t/s), finish: stop

## Prompt

Give the single kubectl command to list all pods in the namespace `prod`, sorted by creation timestamp. Reply with ONLY the command in a code block.

## Answer

```bash
kubectl get pods -n prod --sort=metadata.creationTimestamp
```
