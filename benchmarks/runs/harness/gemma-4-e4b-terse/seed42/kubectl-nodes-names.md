# gemma-4-e4b-terse / kubectl-nodes-names / seed 42 / harness

## Prompt

Give the single kubectl command that prints only the names of all nodes in the cluster, using jsonpath output. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 23 tokens in 6.8s, finish: stop
- verifier: pass

```bash
kubectl get nodes -o=jsonpath='{.items[*].metadata.name}'
```
