# qwen2.5-coder-7b / sh-distinct-words / seed 42 / harness

## Prompt

The file `text.txt` contains words separated by spaces and newlines. Print the number of distinct words, ignoring case, and nothing else. Reply with ONLY the bash command (a one-liner or pipeline) in a code block.

## Attempt 1: PASS (hidden: output matches)

- 49 tokens in 12.9s, finish: stop
- verifier: pass

```bash
tr ' ' '\n' < text.txt | tr '\n' ' ' | awk '{for(i=1;i<=NF;i++) a[tolower($i)]++} END{print length(a)}'
```
