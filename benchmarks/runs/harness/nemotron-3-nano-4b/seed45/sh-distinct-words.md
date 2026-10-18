# nemotron-3-nano-4b / sh-distinct-words / seed 45 / harness

## Prompt

The file `text.txt` contains words separated by spaces and newlines. Print the number of distinct words, ignoring case, and nothing else. Reply with ONLY the bash command (a one-liner or pipeline) in a code block.

## Attempt 1: FAIL (hidden: output ['3'], expected ['9'])

- 29 tokens in 6.1s, finish: stop
- verifier: pass

```bash
cat text.txt | tr '[:upper:]' '[:lower:]' | sort -u | wc -l
```
