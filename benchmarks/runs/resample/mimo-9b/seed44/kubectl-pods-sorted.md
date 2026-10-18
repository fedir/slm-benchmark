# mimo-9b / kubectl-pods-sorted / seed 44 / resample (no feedback)

## Prompt

Give the single kubectl command to list all pods in the namespace `prod`, sorted by creation timestamp. Reply with ONLY the command in a code block.

## Attempt 1: FAIL (hidden: missing ['--sort-by[ =]\\.?metadata\\.creationTimestamp'])

- 32 tokens in 10.8s, finish: stop
- verifier: FAIL: kubectl rejected the command: error: unknown flag: --sort

```bash
kubectl get pods -n prod -o custom-columns=NAME:.metadata.name,CREATED:.metadata.creationTimestamp --sort=created
```

## Attempt 2: FAIL (hidden: missing ['--sort-by[ =]\\.?metadata\\.creationTimestamp'])

- 18 tokens in 7.3s, finish: stop
- verifier: FAIL: kubectl rejected the command: error: unknown flag: --sort

```
kubectl -n prod get pods --sort='metadata.creationTimestamp'
```

## Attempt 3: FAIL (hidden: missing ['--sort-by[ =]\\.?metadata\\.creationTimestamp'])

- 34 tokens in 11.7s, finish: stop
- verifier: FAIL: kubectl rejected the command: error: unknown flag: --sort

```bash
kubectl get pods -n prod -o custom-columns=NAME:.metadata.name,CREATED:.metadata.creationTimestamp --sort=.metadata.creationTimestamp
```
