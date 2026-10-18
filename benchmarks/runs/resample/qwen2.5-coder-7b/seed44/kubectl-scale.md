# qwen2.5-coder-7b / kubectl-scale / seed 44 / resample (no feedback)

## Prompt

Give the single kubectl command to scale the deployment `web` in namespace `staging` to 5 replicas. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 18 tokens in 5.6s, finish: stop
- verifier: pass

```bash
kubectl scale deployment web --replicas=5 -n staging
```
