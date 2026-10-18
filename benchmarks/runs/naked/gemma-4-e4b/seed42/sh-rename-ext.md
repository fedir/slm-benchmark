# gemma-4-e4b / sh-rename-ext / seed 42 / naked

## Prompt

The current directory contains some `.txt` files and other files. Rename every `.txt` file to the same name with the extension `.md`. Reply with ONLY the bash command (a one-liner or pipeline) in a code block.

## Attempt 1: PASS (hidden: output matches)

- 25 tokens in 5.5s, finish: stop

```bash
for file in *.txt; do mv "$file" "${file%.txt}.md"; done
```
