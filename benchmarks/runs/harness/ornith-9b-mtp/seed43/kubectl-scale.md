# ornith-9b-mtp / kubectl-scale / seed 43 / harness

## Prompt

Give the single kubectl command to scale the deployment `web` in namespace `staging` to 5 replicas. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 18 tokens in 6.4s, finish: stop
- verifier: pass

```bash
kubectl scale deployment web --namespace staging --replicas=5
```
