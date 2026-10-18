# nemotron-3-nano-4b / regex-semver / seed 45 / harness

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a version `MAJOR.MINOR.PATCH` where each part is a non-negative integer without leading zeros (so `0` is allowed, `01` is not). Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: invalid regex '^0|[1-9]\\d*\\.0|[1-9]\\d*\\.\\d+$|[1-9]\\d*\\.\\d+\\.\\d+$|[1-9]\\d*\\.\\d+\\.\\d+$?$': nothing to repeat at position 69)

- 61 tokens in 11.2s, finish: stop
- verifier: FAIL: invalid regex '^0|[1-9]\\d*\\.0|[1-9]\\d*\\.\\d+$|[1-9]\\d*\\.\\d+\\.\\d+$|[1-9]\\d*\\.\\d+\\.\\d+$?$': nothing to repeat at position 69

```python
^0|[1-9]\d*\.0|[1-9]\d*\.\d+$|[1-9]\d*\.\d+\.\d+$|[1-9]\d*\.\d+\.\d+$?$
```

## Attempt 2: FAIL (hidden: regex '^(0|[1-9]\\d*)\\.0|(0|[1-9]\\d*)\\.([1-9]\\d*)|(0|[1-9]\\d*)\\.([1-9]\\d*)\\.([1-9]\\d*)$'; wrong on ['0.0.0', '100.0.1', '!1.2'])

- 64 tokens in 14.6s, finish: stop
- verifier: FAIL: it does not match these, which it should: ['2.0.15', '0.10.0']; it matches these, which it must reject: ['4.5']

```python
^(0|[1-9]\d*)\.0|(0|[1-9]\d*)\.([1-9]\d*)|(0|[1-9]\d*)\.([1-9]\d*)\.([1-9]\d*)$
```

## Attempt 3: FAIL (hidden: regex '^(0|[1-9]\\d*)\\.0|(0|[1-9]\\d*)\\.([1-9]\\d*)|(0|[1-9]\\d*)\\.([1-9]\\d*)\\.([1-9]\\d*)$'; wrong on ['0.0.0', '100.0.1', '!1.2'])

- 64 tokens in 17.6s, finish: stop
- verifier: FAIL: it does not match these, which it should: ['2.0.15', '0.10.0']; it matches these, which it must reject: ['4.5']

```python
^(0|[1-9]\d*)\.0|(0|[1-9]\d*)\.([1-9]\d*)|(0|[1-9]\d*)\.([1-9]\d*)\.([1-9]\d*)$
```
