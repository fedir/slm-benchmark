# gemma-4-e4b / kubectl-events-sorted / seed 42 / naked

## Prompt

Give the single kubectl command to list the events in namespace `prod` sorted by their last timestamp. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 20 tokens in 4.8s, finish: stop

```bash
kubectl get events --namespace prod --sort-by='.lastTimestamp'
```
