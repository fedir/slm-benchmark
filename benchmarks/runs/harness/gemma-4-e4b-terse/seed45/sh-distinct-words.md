# gemma-4-e4b-terse / sh-distinct-words / seed 45 / harness

## Prompt

The file `text.txt` contains words separated by spaces and newlines. Print the number of distinct words, ignoring case, and nothing else. Reply with ONLY the bash command (a one-liner or pipeline) in a code block.

## Attempt 1: PASS (hidden: output matches)

- 44 tokens in 9.8s, finish: stop
- verifier: pass

```bash
tr '[:upper:]' '[:lower:]' < text.txt | tr -s ' ' '\n' | grep -v '^$' | sort -u | wc -l
```
