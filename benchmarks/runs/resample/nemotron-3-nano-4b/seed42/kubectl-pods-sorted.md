# nemotron-3-nano-4b / kubectl-pods-sorted / seed 42 / resample (no feedback)

## Prompt

Give the single kubectl command to list all pods in the namespace `prod`, sorted by creation timestamp. Reply with ONLY the command in a code block.

## Attempt 1: FAIL (hidden: missing ['--sort-by[ =]\\.?metadata\\.creationTimestamp'])

- 46 tokens in 8.0s, finish: stop
- verifier: FAIL: it must be a single kubectl invocation: no pipes, redirects or substitutions

```bash
kubectl get pods -n prod -o jsonpath='{range .items[0]}={{.metadata.name}} {{.metadata.createTime}} {end}' | sort -k2 -r
```

## Attempt 2: PASS (hidden: all parts present)

- 21 tokens in 5.1s, finish: stop
- verifier: pass

```bash
kubectl get pods -n prod --sort-by=.metadata.creationTimestamp
```
