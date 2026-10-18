# qwen2.5-coder-3b / kubectl-nodes-names

- category: kubectl
- result: **PASS** (all parts present)
- tokens: 30 in 3s (8.7 t/s), finish: stop

## Prompt

Give the single kubectl command that prints only the names of all nodes in the cluster, using jsonpath output. Reply with ONLY the command in a code block.

## Answer

```sh
kubectl get nodes -o jsonpath='{range .items[*]}{.metadata.name}{"\n"}{end}'
```
