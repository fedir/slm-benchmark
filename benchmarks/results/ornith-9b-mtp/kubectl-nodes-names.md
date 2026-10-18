# ornith-9b-mtp / kubectl-nodes-names

- category: kubectl
- result: **PASS** (all parts present)
- tokens: 29 in 162s (0.2 t/s), finish: stop

## Prompt

Give the single kubectl command that prints only the names of all nodes in the cluster, using jsonpath output. Reply with ONLY the command in a code block.

## Answer

```
kubectl get nodes -o jsonpath='{range .items[*]}{.metadata.name}{"\n"}{end}'
```
