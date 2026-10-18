# nemotron-3-nano-4b / kubectl-pods-sorted / seed 44 / harness

## Prompt

Give the single kubectl command to list all pods in the namespace `prod`, sorted by creation timestamp. Reply with ONLY the command in a code block.

## Attempt 1: FAIL (hidden: missing ['--sort-by[ =]\\.?metadata\\.creationTimestamp'])

- 19 tokens in 4.5s, finish: stop
- verifier: pass

```bash
kubectl get pods -n prod --sort-by=creationTimestamp
```
