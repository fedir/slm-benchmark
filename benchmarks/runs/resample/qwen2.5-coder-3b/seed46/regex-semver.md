# qwen2.5-coder-3b / regex-semver / seed 46 / resample (no feedback)

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a version `MAJOR.MINOR.PATCH` where each part is a non-negative integer without leading zeros (so `0` is allowed, `01` is not). Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: regex '\\b\\d+\\.\\d+\\.\\d+\\b'; wrong on ['!01.2.3', '!1.02.3', '!1.2.03'])

- 15 tokens in 2.9s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['3.04.5', '10.0.00']

```
\b\d+\.\d+\.\d+\b
```

## Attempt 2: FAIL (hidden: regex "r'^\\d+\\.\\d+\\.\\d+$"; wrong on ['0.0.0', '1.2.3', '10.20.30', '100.0.1'])

- 16 tokens in 3.0s, finish: stop
- verifier: FAIL: it does not match these, which it should: ['2.0.15', '0.10.0', '7.7.7']

```
r'^\d+\.\d+\.\d+$
```

## Attempt 3: FAIL (hidden: regex '^\\d+\\.\\d+\\.\\d+$'; wrong on ['!01.2.3', '!1.02.3', '!1.2.03'])

- 17 tokens in 3.1s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['3.04.5', '10.0.00']

```python
r'^\d+\.\d+\.\d+$'
```
