# qwen2.5-coder-3b / sh-distinct-words / seed 43 / harness

## Prompt

The file `text.txt` contains words separated by spaces and newlines. Print the number of distinct words, ignoring case, and nothing else. Reply with ONLY the bash command (a one-liner or pipeline) in a code block.

## Attempt 1: PASS (hidden: output matches)

- 37 tokens in 4.9s, finish: stop
- verifier: pass

```bash
tr '[:upper:]' '[:lower:]' < text.txt | tr -s ' ' '\n' | sort | uniq | wc -l
```
