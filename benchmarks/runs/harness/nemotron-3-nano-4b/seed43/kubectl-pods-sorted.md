# nemotron-3-nano-4b / kubectl-pods-sorted / seed 43 / harness

## Prompt

Give the single kubectl command to list all pods in the namespace `prod`, sorted by creation timestamp. Reply with ONLY the command in a code block.

## Attempt 1: FAIL (hidden: missing ['--sort-by[ =]\\.?metadata\\.creationTimestamp'])

- 49 tokens in 8.5s, finish: stop
- verifier: FAIL: it must be a single kubectl invocation: no pipes, redirects or substitutions

```bash
kubectl get pods -n prod -o json | jq -r '.items[] | "\(.metadata.creationTimestamp) \(.metadata.name)"' | sort | cut -d' ' -f2-
```

## Attempt 2: PASS (hidden: all parts present)

- 22 tokens in 6.9s, finish: stop
- verifier: pass

```bash
kubectl get pods -n prod --sort-by='.metadata.creationTimestamp'
```
