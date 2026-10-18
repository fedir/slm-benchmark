# nemotron-3-nano-4b / sh-distinct-words / seed 44 / harness

## Prompt

The file `text.txt` contains words separated by spaces and newlines. Print the number of distinct words, ignoring case, and nothing else. Reply with ONLY the bash command (a one-liner or pipeline) in a code block.

## Attempt 1: FAIL (hidden: output ['3'], expected ['9'])

- 28 tokens in 5.8s, finish: stop
- verifier: pass

```bash
tr '[:upper:]' '[:lower:]' < text.txt | sort -u | wc -l
```
