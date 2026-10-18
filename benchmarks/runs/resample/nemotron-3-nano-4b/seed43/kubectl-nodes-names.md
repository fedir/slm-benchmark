# nemotron-3-nano-4b / kubectl-nodes-names / seed 43 / resample (no feedback)

## Prompt

Give the single kubectl command that prints only the names of all nodes in the cluster, using jsonpath output. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 22 tokens in 4.9s, finish: stop
- verifier: pass

```bash
kubectl get nodes -o jsonpath='{.items[].metadata.name}'
```
