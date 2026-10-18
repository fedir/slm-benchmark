# ornith-9b-mtp / kubectl-events-sorted / seed 42 / harness

## Prompt

Give the single kubectl command to list the events in namespace `prod` sorted by their last timestamp. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 18 tokens in 6.3s, finish: stop
- verifier: pass

```bash
kubectl get events -n prod --sort-by=.lastTimestamp
```
