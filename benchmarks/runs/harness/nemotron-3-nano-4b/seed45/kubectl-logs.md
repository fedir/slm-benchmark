# nemotron-3-nano-4b / kubectl-logs / seed 45 / harness

## Prompt

Give the single kubectl command to stream (follow) the last 100 log lines of container `app` in pod `api-0`. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 24 tokens in 5.2s, finish: stop
- verifier: FAIL: the command is valid kubectl but does not do what was asked: the target should be pod `api-0`

```bash
kubectl logs -f api-0/app -c app --tail=100
```

## Attempt 2: PASS (hidden: all parts present)

- 23 tokens in 7.1s, finish: stop
- verifier: pass

```bash
kubectl logs -f api-0 -c app --tail=100
```
