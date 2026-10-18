# nemotron-3-nano-4b / kubectl-logs / seed 44 / harness

## Prompt

Give the single kubectl command to stream (follow) the last 100 log lines of container `app` in pod `api-0`. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 27 tokens in 7.3s, finish: stop
- verifier: pass

```bash
kubectl logs -f pod/api-0 -c app -n default --tail=100
```
