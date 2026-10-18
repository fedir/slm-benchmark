# ornith-9b-mtp / kubectl-rollout-restart / seed 43 / harness

## Prompt

Give the single kubectl command to restart the deployment `api` in namespace `prod` with a rolling restart. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 14 tokens in 5.4s, finish: stop
- verifier: pass

```bash
kubectl rollout restart deployment/api -n prod
```
