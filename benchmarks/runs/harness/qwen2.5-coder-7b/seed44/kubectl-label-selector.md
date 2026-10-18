# qwen2.5-coder-7b / kubectl-label-selector / seed 44 / harness

## Prompt

Give the single kubectl command to list the pods labelled `app=web` in namespace `prod`. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 17 tokens in 5.4s, finish: stop
- verifier: pass

```sh
kubectl get pods -n prod -l app=web
```
