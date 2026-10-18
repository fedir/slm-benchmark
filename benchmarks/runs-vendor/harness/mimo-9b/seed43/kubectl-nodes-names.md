# mimo-9b / kubectl-nodes-names / seed 43 / harness

## Prompt

Give the single kubectl command that prints only the names of all nodes in the cluster, using jsonpath output. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 31 tokens in 10.8s, finish: stop
- verifier: pass

```bash
kubectl get nodes -o jsonpath='{range .items[*]}{.metadata.name}{"\n"}{end}'
```
