# nemotron-3-nano-4b / kubectl-pods-sorted / seed 46 / harness

## Prompt

Give the single kubectl command to list all pods in the namespace `prod`, sorted by creation timestamp. Reply with ONLY the command in a code block.

## Attempt 1: FAIL (hidden: missing ['--sort-by[ =]\\.?metadata\\.creationTimestamp'])

- 48 tokens in 8.5s, finish: stop
- verifier: FAIL: it must be a single kubectl invocation: no pipes, redirects or substitutions

```bash
kubectl get pods -n prod -o jsonpath='{range .items[0]}{{ .metadata.creationTimestamp }} {{ .metadata.name }} {{ end}}' | sort -k1,1
```

## Attempt 2: PASS (hidden: all parts present)

- 21 tokens in 6.9s, finish: stop
- verifier: pass

```bash
kubectl get pods -n prod --sort-by=metadata.creationTimestamp
```
