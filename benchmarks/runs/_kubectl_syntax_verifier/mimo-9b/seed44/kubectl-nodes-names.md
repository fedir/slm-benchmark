# mimo-9b / kubectl-nodes-names / seed 44 / harness

## Prompt

Give the single kubectl command that prints only the names of all nodes in the cluster, using jsonpath output. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 21 tokens in 8.7s, finish: stop
- verifier: pass

```bash
kubectl get nodes -o jsonpath='{.items[*].metadata.name}'
```
