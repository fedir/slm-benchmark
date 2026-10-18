# nemotron-3-nano-4b / kubectl-portforward / seed 46 / resample (no feedback)

## Prompt

Give the single kubectl command to forward local port 8080 to port 80 of the service `web` in namespace `staging`. Reply with ONLY the command in a code block.

## Attempt 1: FAIL (hidden: missing ['-n[ =]?staging\\b'])

- 23 tokens in 5.1s, finish: stop
- verifier: FAIL: the command is valid kubectl but does not do what was asked: the target should be `svc/web`, the command uses 'service/web:80'; the namespace should be `staging`, the command uses None

```bash
kubectl port-forward service/web:80 8080:80
```

## Attempt 2: FAIL (hidden: missing ['-n[ =]?staging\\b'])

- 20 tokens in 5.0s, finish: stop
- verifier: FAIL: kubectl rejected the command: error: TYPE/NAME and list of ports are required for port-forward

```bash
kubectl port-forward service/web:8080:80
```

## Attempt 3: PASS (hidden: all parts present)

- 28 tokens in 5.7s, finish: stop
- verifier: FAIL: the command is valid kubectl but does not do what was asked: the target should be `svc/web`, the command uses 'service/web:80'

```bash
kubectl port-forward service/web:80 8080:80 --namespace=staging
```
