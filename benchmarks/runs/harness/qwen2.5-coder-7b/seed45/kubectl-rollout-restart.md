# qwen2.5-coder-7b / kubectl-rollout-restart / seed 45 / harness

## Prompt

Give the single kubectl command to restart the deployment `api` in namespace `prod` with a rolling restart. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 14 tokens in 4.8s, finish: stop
- verifier: pass

```sh
kubectl rollout restart deployment/api -n prod
```
