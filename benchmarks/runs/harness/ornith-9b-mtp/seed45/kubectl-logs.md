# ornith-9b-mtp / kubectl-logs / seed 45 / harness

## Prompt

Give the single kubectl command to stream (follow) the last 100 log lines of container `app` in pod `api-0`. Reply with ONLY the command in a code block.

## Attempt 1: FAIL (hidden: missing ['-c[ =]?app\\b'])

- 20 tokens in 9.5s, finish: stop
- verifier: FAIL: the command is valid kubectl but does not do what was asked: the target should be pod `api-0`; the container to read should be `app`, the command selects None

```bash
kubectl logs -f api-0/app --tail=100
```

## Attempt 2: FAIL (hidden: missing ['-c[ =]?app\\b'])

- 21 tokens in 13.2s, finish: stop
- verifier: FAIL: kubectl rejected the command: error: arguments in resource/name form may not have more than one slash

```bash
kubectl logs -f pod/api-0/app --tail=100
```

## Attempt 3: PASS (hidden: all parts present)

- 23 tokens in 16.5s, finish: stop
- verifier: FAIL: the command is valid kubectl but does not do what was asked: the target should be pod `api-0`

```bash
kubectl logs -f api-0/app -c app --tail=100
```
