# qwen2.5-coder-3b / kubectl-top / seed 45 / resample (no feedback)

## Prompt

Give the single kubectl command to show the CPU and memory usage of the pods in namespace `prod`, sorted by memory. Reply with ONLY the command in a code block.

## Attempt 1: FAIL (hidden: missing ['top', '--sort-by[ =]memory\\b'])

- 50 tokens in 5.4s, finish: stop
- verifier: FAIL: it must be a single kubectl invocation: no pipes, redirects or substitutions

```sh
kubectl get pods -n prod -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.containerStatuses[*].usage.memory}{\n}' | sort -k2
```

## Attempt 2: FAIL (hidden: missing ['top', '--sort-by[ =]memory\\b'])

- 28 tokens in 3.5s, finish: stop
- verifier: FAIL: the command is valid kubectl but does not do what was asked: the kubectl subcommand should be `top`, not `get`

```bash
kubectl get pods -n prod -o wide --sort-by='.spec.containers[0].resources.requests.memory'
```

## Attempt 3: PASS (hidden: all parts present)

- 17 tokens in 2.5s, finish: stop
- verifier: pass

```bash
kubectl top pod -n prod --sort-by=memory
```
