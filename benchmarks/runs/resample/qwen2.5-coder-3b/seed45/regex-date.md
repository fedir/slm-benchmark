# qwen2.5-coder-3b / regex-date / seed 45 / resample (no feedback)

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches dates in the format YYYY-MM-DD where the month is 01-12 and the day is 01-31 (no need to check month lengths). Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: PASS (hidden: regex '\\b(\\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[12]\\d|3[01])\\b')

- 44 tokens in 5.4s, finish: stop
- verifier: pass

```python
\b(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])\b
```
