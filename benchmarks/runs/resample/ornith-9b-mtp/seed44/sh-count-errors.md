# ornith-9b-mtp / sh-count-errors / seed 44 / resample (no feedback)

## Prompt

The file `app.log` is in the current directory. Print the number of lines that contain the exact word ERROR (uppercase), and nothing else. Reply with ONLY the bash command (a one-liner or pipeline) in a code block.

## Attempt 1: FAIL (hidden: output ['0'], expected ['3'])

- 16 tokens in 6.7s, finish: stop
- verifier: FAIL: on a small example the command's output ['0'], expected ['4']

```bash
grep -c -x -w ERROR app.log
```

## Attempt 2: PASS (hidden: output matches)

- 16 tokens in 6.7s, finish: stop
- verifier: pass

```bash
grep -c '\bERROR\b' app.log
```
