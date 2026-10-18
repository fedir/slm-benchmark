# mimo-9b / kubectl-portforward / seed 43 / harness

## Prompt

Give the single kubectl command to forward local port 8080 to port 80 of the service `web` in namespace `staging`. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 22 tokens in 9.0s, finish: stop
- verifier: pass

```bash
kubectl port-forward svc/web -n staging 8080:80
```
