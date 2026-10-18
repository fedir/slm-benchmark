# nemotron-3-nano-4b / kubectl-scale / seed 45 / resample (no feedback)

## Prompt

Give the single kubectl command to scale the deployment `web` in namespace `staging` to 5 replicas. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 20 tokens in 6.0s, finish: stop
- verifier: pass

```bash
kubectl scale deployment/web -n staging --replicas=5
```
