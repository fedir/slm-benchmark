# nemotron-3-nano-4b / kubectl-scale

- category: kubectl
- result: **PASS** (all parts present)
- tokens: 20 in 4s (4.5 t/s), finish: stop

## Prompt

Give the single kubectl command to scale the deployment `web` in namespace `staging` to 5 replicas. Reply with ONLY the command in a code block.

## Answer

```bash
kubectl scale deployment/web -n staging --replicas=5
```
