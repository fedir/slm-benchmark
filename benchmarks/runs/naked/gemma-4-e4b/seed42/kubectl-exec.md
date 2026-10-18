# gemma-4-e4b / kubectl-exec / seed 42 / naked

## Prompt

Give the single kubectl command to run the command `ls /data` in the container `db` of the pod `db-0` in namespace `data`. Reply with ONLY the command in a code block.

## Attempt 1: FAIL (hidden: missing ['-c[ =]?db\\b'])

- 20 tokens in 4.8s, finish: stop

```bash
kubectl exec -it db-0 -n data -- ls /data
```
