# qwen2.5-coder-7b / regex-slug / seed 45 / harness

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a URL slug: lowercase letters and digits in words separated by single hyphens, with no leading, trailing or doubled hyphen. Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: PASS (hidden: regex '^[a-z0-9]+(-[a-z0-9]+)*$')

- 25 tokens in 8.3s, finish: stop
- verifier: pass

```python
r"^[a-z0-9]+(-[a-z0-9]+)*$"
```
