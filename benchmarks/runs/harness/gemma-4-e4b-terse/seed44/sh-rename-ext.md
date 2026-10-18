# gemma-4-e4b-terse / sh-rename-ext / seed 44 / harness

## Prompt

The current directory contains some `.txt` files and other files. Rename every `.txt` file to the same name with the extension `.md`. Reply with ONLY the bash command (a one-liner or pipeline) in a code block.

## Attempt 1: PASS (hidden: output matches)

- 25 tokens in 7.0s, finish: stop
- verifier: pass

```bash
for f in *.txt; do mv "$f" "${f%.txt}.md"; done
```
