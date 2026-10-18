# ornith-9b-mtp / kubectl-exec / seed 46 / harness

## Prompt

Give the single kubectl command to run the command `ls /data` in the container `db` of the pod `db-0` in namespace `data`. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 20 tokens in 7.8s, finish: stop
- verifier: pass

```
kubectl exec db-0 --namespace data -c db -- ls /data
```
