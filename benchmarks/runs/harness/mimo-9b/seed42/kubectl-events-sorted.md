# mimo-9b / kubectl-events-sorted / seed 42 / harness

## Prompt

Give the single kubectl command to list the events in namespace `prod` sorted by their last timestamp. Reply with ONLY the command in a code block.

## Attempt 1: FAIL (hidden: missing ['--sort-by[ =]\\S*lastTimestamp\\b'])

- 18 tokens in 7.2s, finish: stop
- verifier: FAIL: the command is valid kubectl but does not do what was asked: the --sort-by option should be '.lastTimestamp', the command has '.last_timestamp'

```bash
kubectl get events -n prod --sort-by=.last_timestamp
```

## Attempt 2: PASS (hidden: all parts present)

- 18 tokens in 9.6s, finish: stop
- verifier: pass

```bash
kubectl get events -n prod --sort-by=.lastTimestamp
```
