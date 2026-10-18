# ornith-9b-mtp / kubectl-portforward / seed 46 / harness

## Prompt

Give the single kubectl command to forward local port 8080 to port 80 of the service `web` in namespace `staging`. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 23 tokens in 7.3s, finish: stop
- verifier: FAIL: the command is valid kubectl but does not do what was asked: the target should be `svc/web`, the command uses 'svc/web-staging'

```
kubectl port-forward svc/web-staging 8080:80 -n staging
```

## Attempt 2: PASS (hidden: all parts present)

- 21 tokens in 10.3s, finish: stop
- verifier: pass

```
kubectl port-forward svc/web 8080:80 -n staging
```
