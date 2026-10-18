# mimo-9b / sh-count-errors / seed 43 / harness

## Prompt

The file `app.log` is in the current directory. Print the number of lines that contain the exact word ERROR (uppercase), and nothing else. Reply with ONLY the bash command (a one-liner or pipeline) in a code block.

## Attempt 1: PASS (hidden: output matches)

- 16 tokens in 6.9s, finish: stop
- verifier: pass

```bash
grep -c '\bERROR\b' app.log
```
