# mimo-9b / kubectl-label-selector / seed 42 / harness

## Prompt

Give the single kubectl command to list the pods labelled `app=web` in namespace `prod`. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 17 tokens in 6.9s, finish: stop
- verifier: pass

```bash
kubectl get pods -l app=web -n prod
```
