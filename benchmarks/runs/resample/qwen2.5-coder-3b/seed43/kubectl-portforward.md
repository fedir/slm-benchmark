# qwen2.5-coder-3b / kubectl-portforward / seed 43 / resample (no feedback)

## Prompt

Give the single kubectl command to forward local port 8080 to port 80 of the service `web` in namespace `staging`. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 22 tokens in 3.6s, finish: stop
- verifier: pass

```bash
kubectl port-forward svc/web 8080:80 -n staging
```
