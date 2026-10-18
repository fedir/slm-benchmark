# gemma-4-e4b-concise / kubectl-exec / seed 42 / harness

## Prompt

Give the single kubectl command to run the command `ls /data` in the container `db` of the pod `db-0` in namespace `data`. Reply with ONLY the command in a code block.

## Attempt 1: FAIL (hidden: missing ['-c[ =]?db\\b'])

- 20 tokens in 6.0s, finish: stop
- verifier: FAIL: the command is valid kubectl but does not do what was asked: the --container option should be 'db', the command has None

```bash
kubectl exec -it db-0 -n data -- ls /data
```

## Attempt 2: PASS (hidden: all parts present)

- 23 tokens in 9.0s, finish: stop
- verifier: pass

```bash
kubectl exec -it db-0 -n data -c db -- ls /data
```
