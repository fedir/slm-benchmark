# nemotron-3-nano-4b / kubectl-pods-sorted

- category: kubectl
- result: **FAIL** (missing ['--sort-by[ =]\\.?metadata\\.creationTimestamp'])
- tokens: 46 in 8s (5.6 t/s), finish: stop

## Prompt

Give the single kubectl command to list all pods in the namespace `prod`, sorted by creation timestamp. Reply with ONLY the command in a code block.

## Answer

```bash
kubectl get pods -n prod -o jsonpath='{range .items[0]}={{.metadata.name}} {{.metadata.createTime}} {end}' | sort -k2 -r
```
