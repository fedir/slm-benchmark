# ornith-9b-mtp / kubectl-logs / seed 42 / harness

## Prompt

Give the single kubectl command to stream (follow) the last 100 log lines of container `app` in pod `api-0`. Reply with ONLY the command in a code block.

## Attempt 1: FAIL (hidden: missing ['-c[ =]?app\\b'])

- 20 tokens in 7.1s, finish: stop
- verifier: pass

```bash
kubectl logs -f api-0/app --tail=100
```
