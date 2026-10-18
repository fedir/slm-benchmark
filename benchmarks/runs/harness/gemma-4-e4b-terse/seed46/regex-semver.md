# gemma-4-e4b-terse / regex-semver / seed 46 / harness

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a version `MAJOR.MINOR.PATCH` where each part is a non-negative integer without leading zeros (so `0` is allowed, `01` is not). Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: PASS (hidden: regex '^(?:[1-9]\\d*|0)\\.(?:[1-9]\\d*|0)\\.(?:[1-9]\\d*|0)$')

- 42 tokens in 10.3s, finish: stop
- verifier: pass

```regex
^(?:[1-9]\d*|0)\.(?:[1-9]\d*|0)\.(?:[1-9]\d*|0)$
```
