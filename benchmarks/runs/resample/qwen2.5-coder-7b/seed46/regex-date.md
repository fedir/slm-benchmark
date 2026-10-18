# qwen2.5-coder-7b / regex-date / seed 46 / resample (no feedback)

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches dates in the format YYYY-MM-DD where the month is 01-12 and the day is 01-31 (no need to check month lengths). Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: regex '^\\d{4}-\\d{2}-\\d{2}$'; wrong on ['!2024-13-01', '!2024-00-10', '!2024-01-32', '!2024-01-00'])

- 21 tokens in 7.5s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['2023-15-10', '2023-00-01', '2023-07-45', '2023-07-00']

```python
^\d{4}-\d{2}-\d{2}$
```

## Attempt 2: FAIL (hidden: regex '^\\d{4}-[01]\\d-[0123]\\d$'; wrong on ['!2024-13-01', '!2024-00-10', '!2024-01-32', '!2024-01-00'])

- 23 tokens in 11.0s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['2023-15-10', '2023-00-01', '2023-07-00']

```python
^\d{4}-[01]\d-[0123]\d$
```

## Attempt 3: FAIL (hidden: regex '^\\d{4}-\\d{2}-\\d{2}$'; wrong on ['!2024-13-01', '!2024-00-10', '!2024-01-32', '!2024-01-00'])

- 20 tokens in 10.3s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['2023-15-10', '2023-00-01', '2023-07-45', '2023-07-00']

```
^\d{4}-\d{2}-\d{2}$
```
