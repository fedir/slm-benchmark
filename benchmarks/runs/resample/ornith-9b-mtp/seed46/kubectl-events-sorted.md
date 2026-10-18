# ornith-9b-mtp / kubectl-events-sorted / seed 46 / resample (no feedback)

## Prompt

Give the single kubectl command to list the events in namespace `prod` sorted by their last timestamp. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 17 tokens in 6.7s, finish: stop
- verifier: pass

```
kubectl get events -n prod --sort-by=.lastTimestamp
```
