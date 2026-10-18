# qwen2.5-coder-3b / kubectl-logs

- category: kubectl
- result: **PASS** (all parts present)
- tokens: 26 in 3s (7.6 t/s), finish: stop

## Prompt

Give the single kubectl command to stream (follow) the last 100 log lines of container `app` in pod `api-0`. Reply with ONLY the command in a code block.

## Answer

```sh
kubectl logs -f api-0 app -c app -n default --tail=100
```
