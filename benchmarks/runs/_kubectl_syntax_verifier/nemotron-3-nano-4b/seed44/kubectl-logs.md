# nemotron-3-nano-4b / kubectl-logs / seed 44 / harness

## Prompt

Give the single kubectl command to stream (follow) the last 100 log lines of container `app` in pod `api-0`. Reply with ONLY the command in a code block.

## Attempt 1: FAIL (hidden: missing ['-c[ =]?app\\b'])

- 23 tokens in 5.0s, finish: stop
- verifier: pass

```bash
kubectl logs -f app -n api-0 --tail=100
```
