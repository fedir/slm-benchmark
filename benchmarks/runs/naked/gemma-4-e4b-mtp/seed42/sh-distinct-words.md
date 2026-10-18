# gemma-4-e4b-mtp / sh-distinct-words / seed 42 / naked

## Prompt

The file `text.txt` contains words separated by spaces and newlines. Print the number of distinct words, ignoring case, and nothing else. Reply with ONLY the bash command (a one-liner or pipeline) in a code block.

## Attempt 1: PASS (hidden: output matches)

- 41 tokens in 9.4s, finish: stop

```bash
tr -s '[:space:]' '\n' < text.txt | tr '[:upper:]' '[:lower:]' | sort -u | wc -l
```
