# qwen2.5-coder-7b / sh-count-errors / seed 46 / resample (no feedback)

## Prompt

The file `app.log` is in the current directory. Print the number of lines that contain the exact word ERROR (uppercase), and nothing else. Reply with ONLY the bash command (a one-liner or pipeline) in a code block.

## Attempt 1: PASS (hidden: output matches)

- 17 tokens in 6.7s, finish: stop
- verifier: pass

```bash
grep -c '^\bERROR\b' app.log
```
