# qwen2.5-coder-3b / kubectl-logs / seed 44 / harness

## Prompt

Give the single kubectl command to stream (follow) the last 100 log lines of container `app` in pod `api-0`. Reply with ONLY the command in a code block.

## Attempt 1: FAIL (hidden: missing ['\\s-f\\b'])

- 25 tokens in 3.7s, finish: stop
- verifier: pass

```sh
kubectl logs -n <namespace> api-0 -c app --tail=100
```
