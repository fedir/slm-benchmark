# mimo-9b / kubectl-exec / seed 43 / harness

## Prompt

Give the single kubectl command to run the command `ls /data` in the container `db` of the pod `db-0` in namespace `data`. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 21 tokens in 8.7s, finish: stop
- verifier: pass

```bash
kubectl exec -n data db-0 -c db -- ls /data
```
