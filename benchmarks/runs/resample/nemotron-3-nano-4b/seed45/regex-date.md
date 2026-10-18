# nemotron-3-nano-4b / regex-date / seed 45 / resample (no feedback)

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches dates in the format YYYY-MM-DD where the month is 01-12 and the day is 01-31 (no need to check month lengths). Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: regex '^\\\\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\\\d|3[01])$'; wrong on ['2024-02-29', '1999-12-31', '2000-01-01'])

- 44 tokens in 8.7s, finish: stop
- verifier: FAIL: it does not match these, which it should: ['2023-07-15', '1985-10-31', '2030-12-01']

```python
^\\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\d|3[01])$
```

## Attempt 2: PASS (hidden: regex '\\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\d|3[01])')

- 41 tokens in 8.3s, finish: stop
- verifier: pass

```python
\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])
```
