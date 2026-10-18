# mimo-9b / kubectl-pods-sorted / seed 42 / harness

## Prompt

Give the single kubectl command to list all pods in the namespace `prod`, sorted by creation timestamp. Reply with ONLY the command in a code block.

## Attempt 1: FAIL (hidden: missing ['--sort-by[ =]\\.?metadata\\.creationTimestamp'])

- 18 tokens in 8.1s, finish: stop
- verifier: FAIL: kubectl rejected the command: error: unknown flag: --sort

```bash
kubectl get pods -n prod --sort=metadata.creationTimestamp
```

## Attempt 2: FAIL (hidden: missing ['--sort-by[ =]\\.?metadata\\.creationTimestamp'])

- 35 tokens in 15.7s, finish: stop
- verifier: FAIL: kubectl rejected the command: error: unknown flag: --sort

```bash
kubectl get pods -n prod -o custom-columns=POD:.metadata.name,CREATED:.metadata.creationTimestamp --sort=.metadata.creationTimestamp
```

## Attempt 3: FAIL (hidden: missing ['--sort-by[ =]\\.?metadata\\.creationTimestamp'])

- 22 tokens in 17.3s, finish: stop
- verifier: FAIL: kubectl rejected the command: error: unknown flag: --sort

```bash
kubectl get pods -n prod -o json --sort='metadata.creationTimestamp'
```
