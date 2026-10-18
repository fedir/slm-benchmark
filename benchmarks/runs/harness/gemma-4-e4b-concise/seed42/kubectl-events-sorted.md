# gemma-4-e4b-concise / kubectl-events-sorted / seed 42 / harness

## Prompt

Give the single kubectl command to list the events in namespace `prod` sorted by their last timestamp. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 20 tokens in 5.9s, finish: stop
- verifier: pass

```bash
kubectl get events --namespace prod --sort-by='.lastTimestamp'
```
