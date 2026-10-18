# mimo-9b / kubectl-scale

- category: kubectl
- result: **PASS** (all parts present)
- tokens: 18 in 7s (2.4 t/s), finish: stop

## Prompt

Give the single kubectl command to scale the deployment `web` in namespace `staging` to 5 replicas. Reply with ONLY the command in a code block.

## Answer

```bash
kubectl scale -n staging deployment/web --replicas=5
```
