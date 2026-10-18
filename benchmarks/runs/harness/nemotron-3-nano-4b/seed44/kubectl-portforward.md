# nemotron-3-nano-4b / kubectl-portforward / seed 44 / harness

## Prompt

Give the single kubectl command to forward local port 8080 to port 80 of the service `web` in namespace `staging`. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 26 tokens in 5.6s, finish: stop
- verifier: FAIL: the command is valid kubectl but does not do what was asked: the target should be `svc/web`, the command uses 'service/web:80'

```bash
kubectl port-forward service/web:80 8080:80 -n staging
```

## Attempt 2: PASS (hidden: all parts present)

- 27 tokens in 7.7s, finish: stop
- verifier: FAIL: the command is valid kubectl but does not do what was asked: the target should be `svc/web`, the command uses 'svc/web:80'

```bash
kubectl port-forward svc/web:80 8080:80 -n staging
```

## Attempt 3: PASS (hidden: all parts present)

- 27 tokens in 9.9s, finish: stop
- verifier: FAIL: the command is valid kubectl but does not do what was asked: the target should be `svc/web`, the command uses 'svc/web:80'

```bash
kubectl port-forward svc/web:80 8080:80 -n staging
```
