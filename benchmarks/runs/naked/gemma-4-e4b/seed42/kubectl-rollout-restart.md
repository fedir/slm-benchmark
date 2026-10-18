# gemma-4-e4b / kubectl-rollout-restart / seed 42 / naked

## Prompt

Give the single kubectl command to restart the deployment `api` in namespace `prod` with a rolling restart. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 15 tokens in 4.1s, finish: stop

```bash
kubectl rollout restart deployment/api -n prod
```
