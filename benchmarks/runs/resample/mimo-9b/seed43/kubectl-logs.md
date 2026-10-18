# mimo-9b / kubectl-logs / seed 43 / resample (no feedback)

## Prompt

Give the single kubectl command to stream (follow) the last 100 log lines of container `app` in pod `api-0`. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 27 tokens in 9.7s, finish: stop
- verifier: pass

```bash
kubectl logs -f -n default pod/api-0 --tail=100 --container=app
```
