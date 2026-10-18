# qwen2.5-coder-3b / kubectl-top / seed 46 / harness

## Prompt

Give the single kubectl command to show the CPU and memory usage of the pods in namespace `prod`, sorted by memory. Reply with ONLY the command in a code block.

## Attempt 1: FAIL (hidden: missing ['top', '--sort-by[ =]memory\\b'])

- 57 tokens in 6.0s, finish: stop
- verifier: FAIL: the command is valid kubectl but does not do what was asked: the kubectl subcommand should be `top`, not `get`

```sh
kubectl get pods -n prod -o custom-columns=NAME:.metadata.name,CPUPERC:.status.containerStatuses[*].usage.cpu,MEMORY:.status.containerStatuses[*].usage.memory --sort-by=.status.containerStatuses[*].usage.memory
```

## Attempt 2: PASS (hidden: all parts present)

- 17 tokens in 3.7s, finish: stop
- verifier: pass

```sh
kubectl top pods -n prod --sort-by=memory
```
