# qwen2.5-coder-3b / kubectl-nodes-names / seed 42 / harness

## Prompt

Give the single kubectl command that prints only the names of all nodes in the cluster, using jsonpath output. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 30 tokens in 3.7s, finish: stop
- verifier: pass

```sh
kubectl get nodes -o jsonpath='{range .items[*]}{.metadata.name}{"\n"}{end}'
```
