# qwen2.5-coder-7b / sh-distinct-words / seed 45 / harness

## Prompt

The file `text.txt` contains words separated by spaces and newlines. Print the number of distinct words, ignoring case, and nothing else. Reply with ONLY the bash command (a one-liner or pipeline) in a code block.

## Attempt 1: PASS (hidden: output matches)

- 41 tokens in 11.4s, finish: stop
- verifier: pass

```bash
cat text.txt | tr '[:upper:]' '[:lower:]' | tr -s '[:space:]' '\n' | sort | uniq | wc -l
```
