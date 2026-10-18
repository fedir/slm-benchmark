# ornith-9b-mtp / kubectl-logs

- category: kubectl
- result: **FAIL** (missing ['-c[ =]?app\\b'])
- tokens: 20 in 9s (2.2 t/s), finish: stop

## Prompt

Give the single kubectl command to stream (follow) the last 100 log lines of container `app` in pod `api-0`. Reply with ONLY the command in a code block.

## Answer

```bash
kubectl logs -f api-0/app --tail=100
```
