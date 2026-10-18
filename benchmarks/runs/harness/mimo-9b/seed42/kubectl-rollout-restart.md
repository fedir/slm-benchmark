# mimo-9b / kubectl-rollout-restart / seed 42 / harness

## Prompt

Give the single kubectl command to restart the deployment `api` in namespace `prod` with a rolling restart. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 14 tokens in 6.2s, finish: stop
- verifier: pass

```bash
kubectl -n prod rollout restart deployment api
```
