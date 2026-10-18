# gemma-4-e4b-mtp / kubectl-scale / seed 42 / naked

## Prompt

Give the single kubectl command to scale the deployment `web` in namespace `staging` to 5 replicas. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 18 tokens in 4.7s, finish: stop

```bash
kubectl scale deployment web --replicas=5 -n staging
```
