# nemotron-3-nano-4b / regex-date / seed 46 / harness

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches dates in the format YYYY-MM-DD where the month is 01-12 and the day is 01-31 (no need to check month lengths). Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: invalid regex '^(?:\\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\\d|3[01])$': missing ), unterminated subpattern at position 1)

- 46 tokens in 9.1s, finish: stop
- verifier: FAIL: invalid regex '^(?:\\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\\d|3[01])$': missing ), unterminated subpattern at position 1

```python
^(?:\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])$
```

## Attempt 2: FAIL (hidden: invalid regex '^(?:\\\\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\\\\d|3[01])$': missing ), unterminated subpattern at position 1)

- 47 tokens in 12.1s, finish: stop
- verifier: FAIL: invalid regex '^(?:\\\\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\\\\d|3[01])$': missing ), unterminated subpattern at position 1

```python
^(?:\\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\\d|3[01])$
```

## Attempt 3: FAIL (hidden: invalid regex '^(?:\\\\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\\\\d|3[01])$': missing ), unterminated subpattern at position 1)

- 47 tokens in 15.2s, finish: stop
- verifier: FAIL: invalid regex '^(?:\\\\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\\\\d|3[01])$': missing ), unterminated subpattern at position 1

```python
^(?:\\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\\d|3[01])$
```
