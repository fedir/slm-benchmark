# ornith-9b-mtp / kubectl-scale

- category: kubectl
- result: **PASS** (all parts present)
- tokens: 18 in 8s (2.3 t/s), finish: stop

## Prompt

Give the single kubectl command to scale the deployment `web` in namespace `staging` to 5 replicas. Reply with ONLY the command in a code block.

## Answer

```bash
kubectl scale deployment web --namespace staging --replicas 5
```
