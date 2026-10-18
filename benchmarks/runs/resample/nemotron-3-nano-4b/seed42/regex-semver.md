# nemotron-3-nano-4b / regex-semver / seed 42 / resample (no feedback)

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a version `MAJOR.MINOR.PATCH` where each part is a non-negative integer without leading zeros (so `0` is allowed, `01` is not). Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: regex '\\b0(?:\\.[1-9]\\d*|\\.0)*\\b'; wrong on ['1.2.3', '10.20.30', '100.0.1'])

- 22 tokens in 6.0s, finish: stop
- verifier: FAIL: it does not match these, which it should: ['2.0.15', '7.7.7']

```
\b0(?:\.[1-9]\d*|\.0)*\b
```

## Attempt 2: PASS (hidden: regex '^(0|[1-9]\\d*)\\.(0|[1-9]\\d*)\\.(0|[1-9]\\d*)$')

- 38 tokens in 8.0s, finish: stop
- verifier: pass

```python
^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$
```
