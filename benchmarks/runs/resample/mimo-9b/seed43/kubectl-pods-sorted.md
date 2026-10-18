# mimo-9b / kubectl-pods-sorted / seed 43 / resample (no feedback)

## Prompt

Give the single kubectl command to list all pods in the namespace `prod`, sorted by creation timestamp. Reply with ONLY the command in a code block.

## Attempt 1: FAIL (hidden: missing ['--sort-by[ =]\\.?metadata\\.creationTimestamp'])

- 35 tokens in 11.5s, finish: stop
- verifier: FAIL: kubectl rejected the command: error: unknown flag: --sort

```bash
kubectl get pods -n prod -o custom-columns='NAME:.metadata.name,CREATED:.metadata.creationTimestamp' --sort=.metadata.creationTimestamp
```

## Attempt 2: FAIL (hidden: missing ['--sort-by[ =]\\.?metadata\\.creationTimestamp'])

- 35 tokens in 11.8s, finish: stop
- verifier: FAIL: kubectl rejected the command: error: unknown flag: --sort

```bash
kubectl get pods -n prod -o custom-columns=POD:.metadata.name,CREATED:.metadata.creationTimestamp --sort=created:desc
```

## Attempt 3: FAIL (hidden: missing ['--sort-by[ =]\\.?metadata\\.creationTimestamp'])

- 21 tokens in 8.2s, finish: stop
- verifier: FAIL: kubectl rejected the command: error: unknown flag: --sort

```bash
kubectl get pods -n prod --sort='metadata.creationTimestamp,asc'
```
