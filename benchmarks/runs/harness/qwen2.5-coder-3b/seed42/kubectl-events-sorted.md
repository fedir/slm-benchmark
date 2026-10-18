# qwen2.5-coder-3b / kubectl-events-sorted / seed 42 / harness

## Prompt

Give the single kubectl command to list the events in namespace `prod` sorted by their last timestamp. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 19 tokens in 2.9s, finish: stop
- verifier: pass

```bash
kubectl get events --namespace=prod --sort-by='.lastTimestamp'
```
