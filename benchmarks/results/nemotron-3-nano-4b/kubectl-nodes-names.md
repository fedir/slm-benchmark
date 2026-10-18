# nemotron-3-nano-4b / kubectl-nodes-names

- category: kubectl
- result: **PASS** (all parts present)
- tokens: 31 in 6s (5.2 t/s), finish: stop

## Prompt

Give the single kubectl command that prints only the names of all nodes in the cluster, using jsonpath output. Reply with ONLY the command in a code block.

## Answer

```bash
kubectl get nodes -o jsonpath='{range .items[*]}{.metadata.name}{"\n"}{end}'
```
