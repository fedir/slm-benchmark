# mimo-9b / kubectl-nodes-names

- category: kubectl
- result: **PASS** (all parts present)
- tokens: 21 in 8s (2.5 t/s), finish: stop

## Prompt

Give the single kubectl command that prints only the names of all nodes in the cluster, using jsonpath output. Reply with ONLY the command in a code block.

## Answer

```bash
kubectl get nodes -o jsonpath='{.items[*].metadata.name}'
```
