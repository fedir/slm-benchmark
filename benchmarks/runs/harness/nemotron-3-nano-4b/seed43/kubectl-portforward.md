# nemotron-3-nano-4b / kubectl-portforward / seed 43 / harness

## Prompt

Give the single kubectl command to forward local port 8080 to port 80 of the service `web` in namespace `staging`. Reply with ONLY the command in a code block.

## Attempt 1: FAIL (hidden: missing ['\\b8080:80\\b', '-n[ =]?staging\\b'])

- 28 tokens in 5.9s, finish: stop
- verifier: FAIL: the command is valid kubectl but does not do what was asked: the target should be `svc/web`, the command uses 'service/web:80'; the ports should be LOCAL:REMOTE = 8080:80, the command uses '0.0.0.0:8080'; the namespace should be `staging`, the command uses None

```bash
kubectl port-forward service/web:80 0.0.0.0:8080
```

## Attempt 2: FAIL (hidden: missing ['\\b8080:80\\b', '-n[ =]?staging\\b'])

- 29 tokens in 8.8s, finish: stop
- verifier: FAIL: the command is valid kubectl but does not do what was asked: the target should be `svc/web`, the command uses 'svc/web:80'; the ports should be LOCAL:REMOTE = 8080:80, the command uses '0.0.0.0:8080'; the namespace should be `staging`, the command uses None

```bash
kubectl port-forward svc/web:80 0.0.0.0:8080
```

## Attempt 3: FAIL (hidden: missing ['\\b8080:80\\b'])

- 32 tokens in 12.3s, finish: stop
- verifier: FAIL: the command is valid kubectl but does not do what was asked: the target should be `svc/web`, the command uses 'svc/web:80'; the ports should be LOCAL:REMOTE = 8080:80, the command uses '0.0.0.0:8080'

```bash
kubectl port-forward svc/web:80 0.0.0.0:8080 --namespace staging
```
