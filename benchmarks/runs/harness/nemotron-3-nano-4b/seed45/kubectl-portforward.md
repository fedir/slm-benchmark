# nemotron-3-nano-4b / kubectl-portforward / seed 45 / harness

## Prompt

Give the single kubectl command to forward local port 8080 to port 80 of the service `web` in namespace `staging`. Reply with ONLY the command in a code block.

## Attempt 1: FAIL (hidden: missing ['-n[ =]?staging\\b'])

- 23 tokens in 5.2s, finish: stop
- verifier: FAIL: the command is valid kubectl but does not do what was asked: the target should be `svc/web`, the command uses 'service/web:80'; the namespace should be `staging`, the command uses None

```bash
kubectl port-forward service/web:80 8080:80
```

## Attempt 2: PASS (hidden: all parts present)

- 29 tokens in 8.6s, finish: stop
- verifier: FAIL: the command is valid kubectl but does not do what was asked: the target should be `svc/web`, the command uses 'svc/web:80'

```bash
kubectl port-forward svc/web:80 8080:80 --namespace=staging
```

## Attempt 3: FAIL (hidden: missing ['-n[ =]?staging\\b'])

- 24 tokens in 10.1s, finish: stop
- verifier: FAIL: the command is valid kubectl but does not do what was asked: the target should be `svc/web`, the command uses 'svc/web:80'; the namespace should be `staging`, the command uses None

```bash
kubectl port-forward svc/web:80 8080:80
```
