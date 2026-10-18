# qwen2.5-coder-7b / kubectl-logs / seed 42 / resample (no feedback)

## Prompt

Give the single kubectl command to stream (follow) the last 100 log lines of container `app` in pod `api-0`. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 21 tokens in 8.0s, finish: stop
- verifier: pass

```
kubectl logs api-0 -c app --tail=100 --follow
```
