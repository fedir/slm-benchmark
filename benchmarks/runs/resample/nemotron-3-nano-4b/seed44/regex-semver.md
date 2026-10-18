# nemotron-3-nano-4b / regex-semver / seed 44 / resample (no feedback)

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a version `MAJOR.MINOR.PATCH` where each part is a non-negative integer without leading zeros (so `0` is allowed, `01` is not). Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: PASS (hidden: regex '^(0|[1-9]\\d*)\\.(0|[1-9]\\d*)\\.(0|[1-9]\\d*)$')

- 38 tokens in 9.9s, finish: stop
- verifier: pass

```python
^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$
```
