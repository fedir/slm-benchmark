# qwen2.5-coder-3b / kubectl-logs / seed 45 / resample (no feedback)

## Prompt

Give the single kubectl command to stream (follow) the last 100 log lines of container `app` in pod `api-0`. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 25 tokens in 3.8s, finish: stop
- verifier: pass

```bash
kubectl logs -n <namespace> api-0 app --tail=100 --follow
```
