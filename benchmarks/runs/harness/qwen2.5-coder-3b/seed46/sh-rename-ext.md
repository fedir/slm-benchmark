# qwen2.5-coder-3b / sh-rename-ext / seed 46 / harness

## Prompt

The current directory contains some `.txt` files and other files. Rename every `.txt` file to the same name with the extension `.md`. Reply with ONLY the bash command (a one-liner or pipeline) in a code block.

## Attempt 1: PASS (hidden: output matches)

- 25 tokens in 3.8s, finish: stop
- verifier: pass

```bash
for i in *.txt; do mv "$i" "${i%.txt}.md"; done
```
