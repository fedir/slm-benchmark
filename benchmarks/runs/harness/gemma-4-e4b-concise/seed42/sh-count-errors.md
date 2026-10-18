# gemma-4-e4b-concise / sh-count-errors / seed 42 / harness

## Prompt

The file `app.log` is in the current directory. Print the number of lines that contain the exact word ERROR (uppercase), and nothing else. Reply with ONLY the bash command (a one-liner or pipeline) in a code block.

## Attempt 1: FAIL (hidden: output ['0'], expected ['3'])

- 15 tokens in 5.2s, finish: stop
- verifier: FAIL: on a small example the command's output ['0'], expected ['4']

```bash
grep -c "^ERROR$" app.log
```

## Attempt 2: FAIL (hidden: output ['4'], expected ['3'])

- 15 tokens in 7.9s, finish: stop
- verifier: pass

```bash
grep -c "ERROR" app.log
```
