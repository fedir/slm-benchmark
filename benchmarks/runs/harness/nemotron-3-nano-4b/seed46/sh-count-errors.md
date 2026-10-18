# nemotron-3-nano-4b / sh-count-errors / seed 46 / harness

## Prompt

The file `app.log` is in the current directory. Print the number of lines that contain the exact word ERROR (uppercase), and nothing else. Reply with ONLY the bash command (a one-liner or pipeline) in a code block.

## Attempt 1: FAIL (hidden: output ['4'], expected ['3'])

- 14 tokens in 3.9s, finish: stop
- verifier: pass

```bash
grep -c 'ERROR' app.log
```
