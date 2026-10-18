# nemotron-3-nano-4b / kubectl-pods-sorted / seed 44 / harness

## Prompt

Give the single kubectl command to list all pods in the namespace `prod`, sorted by creation timestamp. Reply with ONLY the command in a code block.

## Attempt 1: FAIL (hidden: missing ['--sort-by[ =]\\.?metadata\\.creationTimestamp'])

- 19 tokens in 6.6s, finish: stop
- verifier: FAIL: the command is valid kubectl but does not do what was asked: the list is not sorted by the pod creation timestamp (sort expression found: 'creationTimestamp')

```bash
kubectl get pods -n prod --sort-by=creationTimestamp
```

## Attempt 2: FAIL (hidden: missing ['--sort-by[ =]\\.?metadata\\.creationTimestamp'])

- 19 tokens in 7.7s, finish: stop
- verifier: FAIL: the command is valid kubectl but does not do what was asked: the list is not sorted by the pod creation timestamp (sort expression found: 'creationTimestamp')

```bash
kubectl get pods -n prod --sort-by=creationTimestamp
```

## Attempt 3: FAIL (hidden: missing ['--sort-by[ =]\\.?metadata\\.creationTimestamp'])

- 19 tokens in 9.7s, finish: stop
- verifier: FAIL: the command is valid kubectl but does not do what was asked: the list is not sorted by the pod creation timestamp (sort expression found: 'creationTimestamp')

```bash
kubectl get pods -n prod --sort-by=creationTimestamp
```
