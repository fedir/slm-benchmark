# ornith-9b-mtp / kubectl-logs / seed 44 / resample (no feedback)

## Prompt

Give the single kubectl command to stream (follow) the last 100 log lines of container `app` in pod `api-0`. Reply with ONLY the command in a code block.

## Attempt 1: FAIL (hidden: missing ['-c[ =]?app\\b'])

- 20 tokens in 7.0s, finish: stop
- verifier: FAIL: the command is valid kubectl but does not do what was asked: the target should be pod `api-0`; the container to read should be `app`, the command selects None

```bash
kubectl logs -f api-0/app --tail=100
```

## Attempt 2: PASS (hidden: all parts present)

- 26 tokens in 9.4s, finish: stop
- verifier: pass

```
kubectl logs -f -n default pod/api-0 --tail=100 --container=app
```
