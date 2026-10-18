# qwen2.5-coder-7b / kubectl-exec / seed 44 / resample (no feedback)

## Prompt

Give the single kubectl command to run the command `ls /data` in the container `db` of the pod `db-0` in namespace `data`. Reply with ONLY the command in a code block.

## Attempt 1: PASS (hidden: all parts present)

- 21 tokens in 7.5s, finish: stop
- verifier: pass

```sh
kubectl exec -n data db-0 -c db -- ls /data
```
