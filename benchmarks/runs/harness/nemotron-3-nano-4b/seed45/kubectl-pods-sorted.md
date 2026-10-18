# nemotron-3-nano-4b / kubectl-pods-sorted / seed 45 / harness

## Prompt

Give the single kubectl command to list all pods in the namespace `prod`, sorted by creation timestamp. Reply with ONLY the command in a code block.

## Attempt 1: FAIL (hidden: missing ['--sort-by[ =]\\.?metadata\\.creationTimestamp'])

- 43 tokens in 7.8s, finish: stop
- verifier: FAIL: it must be a single kubectl invocation: no pipes, redirects or substitutions

```bash
kubectl get pods -n prod -o jsonpath='{range .items[0..]}{.metadata.creationTimestamp}{"\n"}{end}' | sort -r
```

## Attempt 2: FAIL (hidden: missing ['--sort-by[ =]\\.?metadata\\.creationTimestamp'])

- 19 tokens in 6.6s, finish: stop
- verifier: FAIL: the command is valid kubectl but does not do what was asked: the list is not sorted by the pod creation timestamp (sort expression found: 'creationTimestamp')

```bash
kubectl get pods -n prod --sort-by=creationTimestamp
```

## Attempt 3: FAIL (hidden: missing ['--sort-by[ =]\\.?metadata\\.creationTimestamp'])

- 19 tokens in 8.7s, finish: stop
- verifier: FAIL: the command is valid kubectl but does not do what was asked: the list is not sorted by the pod creation timestamp (sort expression found: 'creationTimestamp')

```bash
kubectl get pods -n prod --sort-by=creationTimestamp
```
