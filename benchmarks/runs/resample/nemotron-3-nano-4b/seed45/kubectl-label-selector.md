# nemotron-3-nano-4b / kubectl-label-selector / seed 45 / resample (no feedback)

## Prompt

Give the single kubectl command to list the pods labelled `app=web` in namespace `prod`. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 18 tokens in 4.3s, finish: stop
- verifier: pass

```bash
kubectl get pods -l app=web -n prod
```
