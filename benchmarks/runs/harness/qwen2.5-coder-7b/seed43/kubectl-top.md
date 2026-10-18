# qwen2.5-coder-7b / kubectl-top / seed 43 / harness

## Prompt

Give the single kubectl command to show the CPU and memory usage of the pods in namespace `prod`, sorted by memory. Reply with ONLY the command in a code block.

## Attempt 1: FAIL (hidden: missing ['--sort-by[ =]memory\\b'])

- 20 tokens in 5.8s, finish: stop
- verifier: FAIL: kubectl rejected the command: error: --sort-by accepts only cpu or memory

```sh
kubectl top pods --namespace=prod --sort-by=.resources.requests.memory
```

## Attempt 2: FAIL (hidden: missing ['--sort-by[ =]memory\\b'])

- 20 tokens in 8.7s, finish: stop
- verifier: FAIL: kubectl rejected the command: error: --sort-by accepts only cpu or memory

```sh
kubectl top pods --namespace=prod --sort-by=.resources.requests.memory
```

## Attempt 3: PASS (hidden: all parts present)

- 18 tokens in 9.7s, finish: stop
- verifier: pass

```sh
kubectl top pods --namespace=prod --sort-by=memory
```
