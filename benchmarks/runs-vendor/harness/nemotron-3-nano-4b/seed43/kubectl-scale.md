# nemotron-3-nano-4b / kubectl-scale / seed 43 / harness

## Prompt

Give the single kubectl command to scale the deployment `web` in namespace `staging` to 5 replicas. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 20 tokens in 4.8s, finish: stop
- verifier: pass

```bash
kubectl scale deployment/web --replicas=5 -n staging
```
