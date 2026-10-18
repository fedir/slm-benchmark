# ornith-9b-mtp / regex-semver / seed 44 / harness

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a version `MAJOR.MINOR.PATCH` where each part is a non-negative integer without leading zeros (so `0` is allowed, `01` is not). Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: regex '^(0|[1-9][0-9]*)$'; wrong on ['0.0.0', '1.2.3', '10.20.30', '100.0.1'])

- 18 tokens in 7.9s, finish: stop
- verifier: FAIL: it does not match these, which it should: ['2.0.15', '0.10.0', '7.7.7']

```regex
^(0|[1-9][0-9]*)$
```

## Attempt 2: PASS (hidden: regex '^(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)$')

- 42 tokens in 14.3s, finish: stop
- verifier: pass

```regex
^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$
```
