# ornith-9b-mtp / kubectl-scale / seed 45 / resample (no feedback)

## Prompt

Give the single kubectl command to scale the deployment `web` in namespace `staging` to 5 replicas. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 17 tokens in 7.2s, finish: stop
- verifier: pass

```
kubectl scale deployment web -n staging --replicas=5
```
