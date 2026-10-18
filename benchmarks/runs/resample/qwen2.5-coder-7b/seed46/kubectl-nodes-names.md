# qwen2.5-coder-7b / kubectl-nodes-names / seed 46 / resample (no feedback)

## Prompt

Give the single kubectl command that prints only the names of all nodes in the cluster, using jsonpath output. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 20 tokens in 5.9s, finish: stop
- verifier: pass

```sh
kubectl get nodes -o jsonpath='{.items[*].metadata.name}'
```
