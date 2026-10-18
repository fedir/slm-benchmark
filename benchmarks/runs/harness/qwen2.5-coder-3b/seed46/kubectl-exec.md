# qwen2.5-coder-3b / kubectl-exec / seed 46 / harness

## Prompt

Give the single kubectl command to run the command `ls /data` in the container `db` of the pod `db-0` in namespace `data`. Reply with ONLY the command in a code block.

## Attempt 1: FAIL (hidden: missing ['-c[ =]?db\\b', '--\\s+ls\\s+/data\\b'])

- 26 tokens in 3.9s, finish: stop
- verifier: FAIL: the command is valid kubectl but does not do what was asked: the command to run should come after `--` and be `ls /data`, found '/bin/bash -c ls /data'; the --container option should be 'db', the command has None

```sh
kubectl exec -it db-0 -n data -- /bin/bash -c "ls /data"
```

## Attempt 2: PASS (hidden: all parts present)

- 23 tokens in 4.2s, finish: stop
- verifier: pass

```sh
kubectl exec -it db-0 -n data --container db -- ls /data
```
