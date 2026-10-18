# nemotron-3-nano-4b / regex-date / seed 44 / harness

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches dates in the format YYYY-MM-DD where the month is 01-12 and the day is 01-31 (no need to check month lengths). Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: regex '^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(0[1-9]|3[01])$'; wrong on ['2024-02-29', '1999-12-31', '2000-01-01', '!24-01-01'])

- 51 tokens in 10.1s, finish: stop
- verifier: FAIL: it does not match these, which it should: ['2023-07-15', '1985-10-31', '2030-12-01']

```python
^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(0[1-9]|3[01])$
```

## Attempt 2: FAIL (hidden: regex '^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(0[1-9]|3[01])$'; wrong on ['2024-02-29', '1999-12-31', '2000-01-01', '!24-01-01'])

- 51 tokens in 12.9s, finish: stop
- verifier: FAIL: it does not match these, which it should: ['2023-07-15', '1985-10-31', '2030-12-01']

```python
^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(0[1-9]|3[01])$
```

## Attempt 3: FAIL (hidden: regex '^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(0[1-9]|3[01])$'; wrong on ['2024-02-29', '1999-12-31', '2000-01-01', '!24-01-01'])

- 51 tokens in 15.8s, finish: stop
- verifier: FAIL: it does not match these, which it should: ['2023-07-15', '1985-10-31', '2030-12-01']

```python
^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(0[1-9]|3[01])$
```
