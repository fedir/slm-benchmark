# mimo-9b / regex-semver / seed 43 / harness

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a version `MAJOR.MINOR.PATCH` where each part is a non-negative integer without leading zeros (so `0` is allowed, `01` is not). Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: regex '^(?:[1-9][0-9]*)(?:\\.[0-9]+){2}$'; wrong on ['0.0.0', '!1.02.3', '!1.2.03'])

- 27 tokens in 11.0s, finish: stop
- verifier: FAIL: it does not match these, which it should: ['0.10.0']; it matches these, which it must reject: ['3.04.5', '10.0.00']

```
^(?:[1-9][0-9]*)(?:\.[0-9]+){2}$
```

## Attempt 2: FAIL (hidden: regex '^[1-9][0-9]*(?:\\.[0-9]+){2}$'; wrong on ['0.0.0', '!1.02.3', '!1.2.03'])

- 24 tokens in 14.3s, finish: stop
- verifier: FAIL: it does not match these, which it should: ['0.10.0']; it matches these, which it must reject: ['3.04.5', '10.0.00']

```
^[1-9][0-9]*(?:\.[0-9]+){2}$
```

## Attempt 3: FAIL (hidden: regex '^[1-9][0-9]*(?:\\.(?:0|[1-9][0-9]*)){2}$'; wrong on ['0.0.0'])

- 31 tokens in 20.2s, finish: stop
- verifier: FAIL: it does not match these, which it should: ['0.10.0']

```
^[1-9][0-9]*(?:\.(?:0|[1-9][0-9]*)){2}$
```
