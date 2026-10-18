# nemotron-3-nano-4b / kubectl-events-sorted / seed 42 / resample (no feedback)

## Prompt

Give the single kubectl command to list the events in namespace `prod` sorted by their last timestamp. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 19 tokens in 4.6s, finish: stop
- verifier: pass

```bash
kubectl get events -n prod --sort-by=.lastTimestamp
```
