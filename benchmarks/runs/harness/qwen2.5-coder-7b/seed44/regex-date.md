# qwen2.5-coder-7b / regex-date / seed 44 / harness

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches dates in the format YYYY-MM-DD where the month is 01-12 and the day is 01-31 (no need to check month lengths). Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: regex '^\\d{4}-([01]\\d|12)-(0[1-9]|[12]\\d|31)$'; wrong on ['!2024-13-01', '!2024-00-10'])

- 34 tokens in 10.6s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['2023-15-10', '2023-00-01']

```python
^\d{4}-([01]\d|12)-(0[1-9]|[12]\d|31)$
```

## Attempt 2: PASS (hidden: regex '^\\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\d|31)$')

- 39 tokens in 14.7s, finish: stop
- verifier: pass

```python
^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|31)$
```
