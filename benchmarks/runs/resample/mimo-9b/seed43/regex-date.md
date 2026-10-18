# mimo-9b / regex-date / seed 43 / resample (no feedback)

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches dates in the format YYYY-MM-DD where the month is 01-12 and the day is 01-31 (no need to check month lengths). Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: regex '^\\d{4}-(0[1-9]|[12]\\d|3[01])-(0[1-9]|[12]\\d|3[01])$'; wrong on ['!2024-13-01'])

- 45 tokens in 15.5s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['2023-15-10']

```
^\d{4}-(0[1-9]|[12]\d|3[01])-(0[1-9]|[12]\d|3[01])$
```

## Attempt 2: PASS (hidden: regex '^\\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$')

- 44 tokens in 15.5s, finish: stop
- verifier: pass


```
^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$
```
