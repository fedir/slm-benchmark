# gemma-4-e4b-concise / kubectl-logs / seed 42 / harness

## Prompt

Give the single kubectl command to stream (follow) the last 100 log lines of container `app` in pod `api-0`. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 22 tokens in 6.0s, finish: stop
- verifier: pass

```bash
kubectl logs -f api-0 -c app --tail=100
```
