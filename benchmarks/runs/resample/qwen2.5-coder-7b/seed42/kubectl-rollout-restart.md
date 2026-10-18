# qwen2.5-coder-7b / kubectl-rollout-restart / seed 42 / resample (no feedback)

## Prompt

Give the single kubectl command to restart the deployment `api` in namespace `prod` with a rolling restart. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 13 tokens in 4.6s, finish: stop
- verifier: pass

```
kubectl rollout restart deployment/api -n prod
```
