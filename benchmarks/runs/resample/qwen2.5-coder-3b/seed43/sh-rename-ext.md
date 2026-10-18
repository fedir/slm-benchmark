# qwen2.5-coder-3b / sh-rename-ext / seed 43 / resample (no feedback)

## Prompt

The current directory contains some `.txt` files and other files. Rename every `.txt` file to the same name with the extension `.md`. Reply with ONLY the bash command (a one-liner or pipeline) in a code block.

## Attempt 1: PASS (hidden: output matches)

- 25 tokens in 3.9s, finish: stop
- verifier: pass

```bash
for file in *.txt; do mv "$file" "${file%.txt}.md"; done
```
