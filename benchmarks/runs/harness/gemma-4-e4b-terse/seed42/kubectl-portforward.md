# gemma-4-e4b-terse / kubectl-portforward / seed 42 / harness

## Prompt

Give the single kubectl command to forward local port 8080 to port 80 of the service `web` in namespace `staging`. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 24 tokens in 6.9s, finish: stop
- verifier: pass

```bash
kubectl port-forward service/web -n staging 8080:80
```
