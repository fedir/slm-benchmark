# nemotron-3-nano-4b / regex-semver / seed 46 / harness

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a version `MAJOR.MINOR.PATCH` where each part is a non-negative integer without leading zeros (so `0` is allowed, `01` is not). Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: regex '^(?!0[0-9])0|(?:[1-9]\\d*)\\.(?:[1-9]\\d*)\\.(?:[1-9]\\d*)$'; wrong on ['0.0.0', '100.0.1'])

- 45 tokens in 8.9s, finish: stop
- verifier: FAIL: it does not match these, which it should: ['2.0.15', '0.10.0']

```python
^(?!0[0-9])0|(?:[1-9]\d*)\.(?:[1-9]\d*)\.(?:[1-9]\d*)$
```

## Attempt 2: FAIL (hidden: regex '^(?:\\d+(?:\\.\\d+)?\\.\\d+)$'; wrong on ['!01.2.3', '!1.02.3', '!1.2.03', '!1.2'])

- 22 tokens in 7.9s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['3.04.5', '4.5', '10.0.00']

```python
^(?:\d+(?:\.\d+)?\.\d+)$
```

## Attempt 3: PASS (hidden: regex '^(0|[1-9]\\d*)\\.(0|[1-9]\\d*)\\.(0|[1-9]\\d*)$')

- 38 tokens in 12.3s, finish: stop
- verifier: pass

```python
^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$
```
