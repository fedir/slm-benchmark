# gemma-4-e4b / kubectl-label-selector / seed 42 / naked

## Prompt

Give the single kubectl command to list the pods labelled `app=web` in namespace `prod`. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 17 tokens in 4.4s, finish: stop

```bash
kubectl get pods -n prod -l app=web
```
