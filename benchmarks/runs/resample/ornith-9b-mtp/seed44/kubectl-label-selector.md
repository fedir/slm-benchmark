# ornith-9b-mtp / kubectl-label-selector / seed 44 / resample (no feedback)

## Prompt

Give the single kubectl command to list the pods labelled `app=web` in namespace `prod`. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 16 tokens in 5.8s, finish: stop
- verifier: pass

```
kubectl get pods -n prod -l app=web
```
