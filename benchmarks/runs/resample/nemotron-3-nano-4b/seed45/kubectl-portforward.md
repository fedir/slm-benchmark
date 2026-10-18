# nemotron-3-nano-4b / kubectl-portforward / seed 45 / resample (no feedback)

## Prompt

Give the single kubectl command to forward local port 8080 to port 80 of the service `web` in namespace `staging`. Reply with ONLY the command in a code block.

## Attempt 1: FAIL (hidden: missing ['-n[ =]?staging\\b'])

- 23 tokens in 5.2s, finish: stop
- verifier: FAIL: the command is valid kubectl but does not do what was asked: the target should be `svc/web`, the command uses 'service/web:80'; the namespace should be `staging`, the command uses None

```bash
kubectl port-forward service/web:80 8080:80
```

## Attempt 2: FAIL (hidden: missing ['-n[ =]?staging\\b'])

- 23 tokens in 5.2s, finish: stop
- verifier: FAIL: the command is valid kubectl but does not do what was asked: the ports should be LOCAL:REMOTE = 8080:80, the command uses 'stg:8080:80'; the namespace should be `staging`, the command uses None

```bash
kubectl port-forward svc/web stg:8080:80
```

## Attempt 3: PASS (hidden: all parts present)

- 23 tokens in 5.2s, finish: stop
- verifier: pass

```bash
kubectl port-forward service/web -n staging 8080:80
```
