# ornith-9b-mtp / sh-distinct-words / seed 42 / harness

## Prompt

The file `text.txt` contains words separated by spaces and newlines. Print the number of distinct words, ignoring case, and nothing else. Reply with ONLY the bash command (a one-liner or pipeline) in a code block.

## Attempt 1: PASS (hidden: output matches)

- 46 tokens in 12.1s, finish: stop
- verifier: pass

```bash
tr '[:upper:]' '[:lower:]' < text.txt | tr -s ' \n' '\n' | grep -v '^$' | sort -u | wc -l
```
