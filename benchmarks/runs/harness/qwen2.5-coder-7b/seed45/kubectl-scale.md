# qwen2.5-coder-7b / kubectl-scale / seed 45 / harness

## Prompt

Give the single kubectl command to scale the deployment `web` in namespace `staging` to 5 replicas. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 18 tokens in 5.6s, finish: stop
- verifier: pass

```sh
kubectl scale deployment/web --replicas=5 -n staging
```
