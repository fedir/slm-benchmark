# qwen2.5-coder-3b / kubectl-label-selector / seed 43 / resample (no feedback)

## Prompt

Give the single kubectl command to list the pods labelled `app=web` in namespace `prod`. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 17 tokens in 2.7s, finish: stop
- verifier: pass

```bash
kubectl get pods -l app=web -n prod
```
