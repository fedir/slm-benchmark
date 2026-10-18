# mimo-9b / kubectl-logs

- category: kubectl
- result: **PASS** (all parts present)
- tokens: 23 in 9s (2.7 t/s), finish: stop

## Prompt

Give the single kubectl command to stream (follow) the last 100 log lines of container `app` in pod `api-0`. Reply with ONLY the command in a code block.

## Answer

```bash
kubectl logs -f pod/api-0 -c app --tail=100
```
