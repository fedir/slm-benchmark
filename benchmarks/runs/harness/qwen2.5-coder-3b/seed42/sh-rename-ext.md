# qwen2.5-coder-3b / sh-rename-ext / seed 42 / harness

## Prompt

The current directory contains some `.txt` files and other files. Rename every `.txt` file to the same name with the extension `.md`. Reply with ONLY the bash command (a one-liner or pipeline) in a code block.

## Attempt 1: PASS (hidden: output matches)

- 13 tokens in 3.1s, finish: stop
- verifier: pass

```bash
rename .txt .md *.txt
```
