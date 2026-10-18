# nemotron-3-nano-4b / regex-semver / seed 45 / resample (no feedback)

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a version `MAJOR.MINOR.PATCH` where each part is a non-negative integer without leading zeros (so `0` is allowed, `01` is not). Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: invalid regex '^0|[1-9]\\d*\\.0|[1-9]\\d*\\.\\d+$|[1-9]\\d*\\.\\d+\\.\\d+$|[1-9]\\d*\\.\\d+\\.\\d+$?$': nothing to repeat at position 69)

- 61 tokens in 11.2s, finish: stop
- verifier: FAIL: invalid regex '^0|[1-9]\\d*\\.0|[1-9]\\d*\\.\\d+$|[1-9]\\d*\\.\\d+\\.\\d+$|[1-9]\\d*\\.\\d+\\.\\d+$?$': nothing to repeat at position 69

```python
^0|[1-9]\d*\.0|[1-9]\d*\.\d+$|[1-9]\d*\.\d+\.\d+$|[1-9]\d*\.\d+\.\d+$?$
```

## Attempt 2: FAIL (hidden: regex '^\\d{1,3}(\\.\\d{1,3}){2}$'; wrong on ['!01.2.3', '!1.02.3', '!1.2.03'])

- 25 tokens in 6.1s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['3.04.5', '10.0.00']

```python
r'^\d{1,3}(\.\d{1,3}){2}$'
```

## Attempt 3: FAIL (hidden: regex '^(?!00)[0-9]+(?:\\.[0-9]+){2}$'; wrong on ['!01.2.3', '!1.02.3', '!1.2.03'])

- 27 tokens in 6.3s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['3.04.5', '10.0.00']

```python
r'^(?!00)[0-9]+(?:\.[0-9]+){2}$'
```
