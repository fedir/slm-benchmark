# qwen2.5-coder-7b / kubectl-rollout-restart / seed 44 / harness

## Prompt

Give the single kubectl command to restart the deployment `api` in namespace `prod` with a rolling restart. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 15 tokens in 5.0s, finish: stop
- verifier: pass

```bash
kubectl rollout restart deployment/api --namespace=prod
```
