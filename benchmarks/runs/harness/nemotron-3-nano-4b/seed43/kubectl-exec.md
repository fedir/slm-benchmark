# nemotron-3-nano-4b / kubectl-exec / seed 43 / harness

## Prompt

Give the single kubectl command to run the command `ls /data` in the container `db` of the pod `db-0` in namespace `data`. Reply with ONLY the command in a code block.

## Attempt 1: FAIL (hidden: missing ['\\bdb-0\\b'])

- 19 tokens in 4.5s, finish: stop
- verifier: FAIL: kubectl rejected the command: error: pod, type/name or --filename must be specified

```bash
kubectl exec -n data -c db -- ls /data
```

## Attempt 2: FAIL (hidden: missing ['\\bdb-0\\b'])

- 19 tokens in 6.5s, finish: stop
- verifier: FAIL: kubectl rejected the command: error: pod, type/name or --filename must be specified

```bash
kubectl exec -n data -c db -- ls /data
```

## Attempt 3: FAIL (hidden: missing ['\\bdb-0\\b'])

- 19 tokens in 8.7s, finish: stop
- verifier: FAIL: kubectl rejected the command: error: pod, type/name or --filename must be specified

```bash
kubectl exec -n data -c db -- ls /data
```
