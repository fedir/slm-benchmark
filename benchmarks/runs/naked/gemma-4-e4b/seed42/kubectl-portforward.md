# gemma-4-e4b / kubectl-portforward / seed 42 / naked

## Prompt

Give the single kubectl command to forward local port 8080 to port 80 of the service `web` in namespace `staging`. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 24 tokens in 5.4s, finish: stop

```bash
kubectl port-forward service/web 8080:80 -n staging
```
