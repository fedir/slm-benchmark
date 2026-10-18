# qwen2.5-coder-7b / kubectl-portforward / seed 42 / harness

## Prompt

Give the single kubectl command to forward local port 8080 to port 80 of the service `web` in namespace `staging`. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 22 tokens in 7.7s, finish: stop
- verifier: pass

```sh
kubectl port-forward service/web 8080:80 -n staging
```
