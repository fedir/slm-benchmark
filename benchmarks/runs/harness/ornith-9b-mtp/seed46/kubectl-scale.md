# ornith-9b-mtp / kubectl-scale / seed 46 / harness

## Prompt

Give the single kubectl command to scale the deployment `web` in namespace `staging` to 5 replicas. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 17 tokens in 6.0s, finish: stop
- verifier: pass

```
kubectl scale deployment web -n staging --replicas=5
```
