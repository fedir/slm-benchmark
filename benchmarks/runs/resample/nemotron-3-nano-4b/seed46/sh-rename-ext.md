# nemotron-3-nano-4b / sh-rename-ext / seed 46 / resample (no feedback)

## Prompt

The current directory contains some `.txt` files and other files. Rename every `.txt` file to the same name with the extension `.md`. Reply with ONLY the bash command (a one-liner or pipeline) in a code block.

## Attempt 1: PASS (hidden: output matches)

- 25 tokens in 5.4s, finish: stop
- verifier: pass

```bash
for f in *.txt; do mv "$f" "${f%.txt}.md"; done
```
