# gemma-4-e4b-terse / sh-rename-ext / seed 45 / harness

## Prompt

The current directory contains some `.txt` files and other files. Rename every `.txt` file to the same name with the extension `.md`. Reply with ONLY the bash command (a one-liner or pipeline) in a code block.

## Attempt 1: PASS (hidden: output matches)

- 41 tokens in 9.3s, finish: stop
- verifier: pass

```bash
find . -maxdepth 1 -type f -name "*.txt" -exec bash -c 'mv "$1" "${1%.txt}.md"' _ {} \;
```
