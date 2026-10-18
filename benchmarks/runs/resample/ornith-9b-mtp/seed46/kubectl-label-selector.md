# ornith-9b-mtp / kubectl-label-selector / seed 46 / resample (no feedback)

## Prompt

Give the single kubectl command to list the pods labelled `app=web` in namespace `prod`. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 17 tokens in 5.7s, finish: stop
- verifier: pass

```bash
kubectl get pods -n prod -l app=web
```
