# nemotron-3-nano-4b / kubectl-top / seed 45 / harness

## Prompt

Give the single kubectl command to show the CPU and memory usage of the pods in namespace `prod`, sorted by memory. Reply with ONLY the command in a code block.

## Attempt 1: FAIL (hidden: missing ['--sort-by[ =]memory\\b'])

- 21 tokens in 4.8s, finish: stop
- verifier: FAIL: it must be a single kubectl invocation: no pipes, redirects or substitutions

```bash
kubectl top pod --namespace=prod | sort -k2 -n
```

## Attempt 2: FAIL (hidden: missing ['--sort-by[ =]memory\\b'])

- 14 tokens in 5.8s, finish: stop
- verifier: FAIL: the command is valid kubectl but does not do what was asked: the --sort-by option should be 'memory', the command has None

```bash
kubectl top pod --namespace=prod
```

## Attempt 3: PASS (hidden: all parts present)

- 19 tokens in 8.0s, finish: stop
- verifier: pass

```bash
kubectl top pod --namespace=prod --sort-by=memory
```
