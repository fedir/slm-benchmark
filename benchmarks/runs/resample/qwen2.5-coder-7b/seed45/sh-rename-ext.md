# qwen2.5-coder-7b / sh-rename-ext / seed 45 / resample (no feedback)

## Prompt

The current directory contains some `.txt` files and other files. Rename every `.txt` file to the same name with the extension `.md`. Reply with ONLY the bash command (a one-liner or pipeline) in a code block.

## Attempt 1: PASS (hidden: output matches)

- 26 tokens in 8.5s, finish: stop
- verifier: pass

```bash
for file in *.txt; do mv -- "$file" "${file%.txt}.md"; done
```
