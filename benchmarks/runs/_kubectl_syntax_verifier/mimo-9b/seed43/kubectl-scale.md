# mimo-9b / kubectl-scale / seed 43 / harness

## Prompt

Give the single kubectl command to scale the deployment `web` in namespace `staging` to 5 replicas. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 18 tokens in 7.4s, finish: stop
- verifier: pass

```bash
kubectl -n staging scale deployment web --replicas=5
```
