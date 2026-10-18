# qwen2.5-coder-3b / kubectl-label-selector / seed 46 / harness

## Prompt

Give the single kubectl command to list the pods labelled `app=web` in namespace `prod`. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 17 tokens in 2.6s, finish: stop
- verifier: pass

```bash
kubectl get pods -n prod -l app=web
```
