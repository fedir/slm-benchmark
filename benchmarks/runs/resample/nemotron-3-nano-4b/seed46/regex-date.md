# nemotron-3-nano-4b / regex-date / seed 46 / resample (no feedback)

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches dates in the format YYYY-MM-DD where the month is 01-12 and the day is 01-31 (no need to check month lengths). Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: invalid regex '^(?:\\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\\d|3[01])$': missing ), unterminated subpattern at position 1)

- 46 tokens in 9.1s, finish: stop
- verifier: FAIL: invalid regex '^(?:\\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\\d|3[01])$': missing ), unterminated subpattern at position 1

```python
^(?:\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])$
```

## Attempt 2: FAIL (hidden: regex '\\b(?:[0-9]{4}-[0-9]{2}-[0-3][0-9])\\b'; wrong on ['!2024-13-01', '!2024-00-10', '!2024-01-32', '!2024-01-00'])

- 35 tokens in 7.5s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['2023-15-10', '2023-00-01', '2023-07-00']

```python
\b(?:[0-9]{4}-[0-9]{2}-[0-3][0-9])\b
```

## Attempt 3: FAIL (hidden: regex '\\b(?:[0-9]{4}-[0-9]{2}-[0-9]{2})\\b'; wrong on ['!2024-13-01', '!2024-00-10', '!2024-01-32', '!2024-01-00'])

- 32 tokens in 7.3s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['2023-15-10', '2023-00-01', '2023-07-45', '2023-07-00']

```python
\b(?:[0-9]{4}-[0-9]{2}-[0-9]{2})\b
```
