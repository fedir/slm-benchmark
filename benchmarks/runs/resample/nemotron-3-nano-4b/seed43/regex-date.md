# nemotron-3-nano-4b / regex-date / seed 43 / resample (no feedback)

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches dates in the format YYYY-MM-DD where the month is 01-12 and the day is 01-31 (no need to check month lengths). Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: regex '^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-(0[1-9]|[12][0-9]|3[01])$'; wrong on ['2024-02-29', '1999-12-31', '2000-01-01'])

- 59 tokens in 10.9s, finish: stop
- verifier: FAIL: it does not match these, which it should: ['2023-07-15', '1985-10-31', '2030-12-01']

```python
^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-(0[1-9]|[12][0-9]|3[01])$
```

## Attempt 2: FAIL (hidden: regex '\\b(?:[0-9]{4}-[0-9]{2}-[0-9]{2})\\b'; wrong on ['!2024-13-01', '!2024-00-10', '!2024-01-32', '!2024-01-00'])

- 30 tokens in 7.5s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['2023-15-10', '2023-00-01', '2023-07-45', '2023-07-00']

```
\b(?:[0-9]{4}-[0-9]{2}-[0-9]{2})\b
```

## Attempt 3: FAIL (hidden: regex '\\b(?:[0-9]{4}-[0-9]{2}-[0-9]{2})\\b'; wrong on ['!2024-13-01', '!2024-00-10', '!2024-01-32', '!2024-01-00'])

- 32 tokens in 9.4s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['2023-15-10', '2023-00-01', '2023-07-45', '2023-07-00']

```python
\b(?:[0-9]{4}-[0-9]{2}-[0-9]{2})\b
```
