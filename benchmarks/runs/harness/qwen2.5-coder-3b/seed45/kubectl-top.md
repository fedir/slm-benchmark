# qwen2.5-coder-3b / kubectl-top / seed 45 / harness

## Prompt

Give the single kubectl command to show the CPU and memory usage of the pods in namespace `prod`, sorted by memory. Reply with ONLY the command in a code block.

## Attempt 1: FAIL (hidden: missing ['top', '--sort-by[ =]memory\\b'])

- 50 tokens in 5.4s, finish: stop
- verifier: FAIL: it must be a single kubectl invocation: no pipes, redirects or substitutions

```sh
kubectl get pods -n prod -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.containerStatuses[*].usage.memory}{\n}' | sort -k2
```

## Attempt 2: PASS (hidden: all parts present)

- 17 tokens in 3.7s, finish: stop
- verifier: pass

```sh
kubectl top pods -n prod --sort-by=memory
```
