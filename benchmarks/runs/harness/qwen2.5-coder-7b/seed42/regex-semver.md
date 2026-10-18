# qwen2.5-coder-7b / regex-semver / seed 42 / harness

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a version `MAJOR.MINOR.PATCH` where each part is a non-negative integer without leading zeros (so `0` is allowed, `01` is not). Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: PASS (hidden: regex '^(0|[1-9]\\d*)\\.(0|[1-9]\\d*)\\.(0|[1-9]\\d*)$')

- 34 tokens in 10.0s, finish: stop
- verifier: pass

```
^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$
```
