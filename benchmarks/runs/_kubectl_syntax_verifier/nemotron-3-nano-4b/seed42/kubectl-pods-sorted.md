# nemotron-3-nano-4b / kubectl-pods-sorted / seed 42 / harness

## Prompt

Give the single kubectl command to list all pods in the namespace `prod`, sorted by creation timestamp. Reply with ONLY the command in a code block.

## Attempt 1: FAIL (hidden: missing ['--sort-by[ =]\\.?metadata\\.creationTimestamp'])

- 46 tokens in 8.2s, finish: stop
- verifier: FAIL: it must be a single kubectl invocation: no pipes, redirects or substitutions

```bash
kubectl get pods -n prod -o jsonpath='{range .items[0]}={{.metadata.name}} {{.metadata.createTime}} {end}' | sort -k2 -r
```

## Attempt 2: FAIL (hidden: missing ['--sort-by[ =]\\.?metadata\\.creationTimestamp'])

- 59 tokens in 12.0s, finish: stop
- verifier: FAIL: it must be a single kubectl invocation: no pipes, redirects or substitutions

```bash
kubectl get pods -n prod --sort-columns <(kubectl get pods -n prod -o jsonpath='{range .items[0]}={{.metadata.name}} {{.metadata.createTime}} {end}' | sort -k2 -r)
```

## Attempt 3: FAIL (hidden: missing ['--sort-by[ =]\\.?metadata\\.creationTimestamp'])

- 19 tokens in 8.8s, finish: stop
- verifier: pass

```bash
kubectl get pods -n prod --sort-by=createTime
```
