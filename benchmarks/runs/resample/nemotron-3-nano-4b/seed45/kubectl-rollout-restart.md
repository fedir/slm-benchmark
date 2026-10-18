# nemotron-3-nano-4b / kubectl-rollout-restart / seed 45 / resample (no feedback)

## Prompt

Give the single kubectl command to restart the deployment `api` in namespace `prod` with a rolling restart. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 16 tokens in 4.1s, finish: stop
- verifier: pass

```bash
kubectl rollout restart deployment/api -n prod
```
