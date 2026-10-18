# mimo-9b / regex-semver / seed 44 / harness

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a version `MAJOR.MINOR.PATCH` where each part is a non-negative integer without leading zeros (so `0` is allowed, `01` is not). Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: regex '^\\d$|\\d+\\d*$'; wrong on ['0.0.0', '1.2.3', '10.20.30', '100.0.1'])

- 129 tokens in 38.6s, finish: stop
- verifier: FAIL: it does not match these, which it should: ['2.0.15', '0.10.0', '7.7.7']

```
^\d$|\d+\d*$
```

Wait, that's wrong. Let me construct it properly.

A non-negative integer without leading zeros: `0` or `[1-9]\d*`.

So the full version: `([1-9]\d*|0)\.([1-9]\d*|0)\.([1-9]\d*|0)`

```
([1-9][0-9]*|0)\.([1-9][0-9]*|0)\.([1-9][0-9]*|0)
```

## Attempt 2: PASS (hidden: regex '([1-9][0-9]*|0)\\.([1-9][0-9]*|0)\\.([1-9][0-9]*|0)')

- 43 tokens in 21.7s, finish: stop
- verifier: pass

```
([1-9][0-9]*|0)\.([1-9][0-9]*|0)\.([1-9][0-9]*|0)
```
