# qwen2.5-coder-3b / regex-ipv4 / seed 43 / resample (no feedback)

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a valid IPv4 address: four decimal numbers 0-255 separated by dots. Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: PASS (hidden: regex '\\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\b')

- 138 tokens in 13.4s, finish: stop
- verifier: pass

```
\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\b
```
