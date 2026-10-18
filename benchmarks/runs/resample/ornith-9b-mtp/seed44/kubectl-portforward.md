# ornith-9b-mtp / kubectl-portforward / seed 44 / resample (no feedback)

## Prompt

Give the single kubectl command to forward local port 8080 to port 80 of the service `web` in namespace `staging`. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 24 tokens in 7.0s, finish: stop
- verifier: FAIL: the command is valid kubectl but does not do what was asked: the target should be `svc/web`, the command uses 'svc/web-staging'

```bash
kubectl port-forward svc/web-staging 8080:80 -n staging
```

## Attempt 2: PASS (hidden: all parts present)

- 23 tokens in 7.5s, finish: stop
- verifier: FAIL: the command is valid kubectl but does not do what was asked: the target should be `svc/web`, the command uses 'svc/web-staging'

```
kubectl port-forward svc/web-staging 8080:80 -n staging
```

## Attempt 3: PASS (hidden: all parts present)

- 24 tokens in 7.1s, finish: stop
- verifier: FAIL: the command is valid kubectl but does not do what was asked: the target should be `svc/web`, the command uses 'svc/web-staging'

```bash
kubectl port-forward svc/web-staging 8080:80 -n staging
```
