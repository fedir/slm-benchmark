# nemotron-3-nano-4b / kubectl-top / seed 45 / resample (no feedback)

## Prompt

Give the single kubectl command to show the CPU and memory usage of the pods in namespace `prod`, sorted by memory. Reply with ONLY the command in a code block.

## Attempt 1: FAIL (hidden: missing ['--sort-by[ =]memory\\b'])

- 21 tokens in 4.8s, finish: stop
- verifier: FAIL: it must be a single kubectl invocation: no pipes, redirects or substitutions

```bash
kubectl top pod --namespace=prod | sort -k2 -n
```

## Attempt 2: FAIL (hidden: missing ['--sort-by[ =]memory\\b'])

- 20 tokens in 4.8s, finish: stop
- verifier: FAIL: it must be a single kubectl invocation: no pipes, redirects or substitutions

```bash
kubectl top pods -n prod | sort -k2 -n
```

## Attempt 3: FAIL (hidden: missing ['--sort-by[ =]memory\\b'])

- 17 tokens in 4.3s, finish: stop
- verifier: FAIL: kubectl rejected the command: error: unknown flag: --sort

```bash
kubectl top pod -n prod --sort=memory
```
