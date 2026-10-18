# qwen2.5-coder-3b / regex-semver / seed 43 / harness

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a version `MAJOR.MINOR.PATCH` where each part is a non-negative integer without leading zeros (so `0` is allowed, `01` is not). Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: regex '^\\d+\\.\\d+\\.\\d+$'; wrong on ['!01.2.3', '!1.02.3', '!1.2.03'])

- 16 tokens in 3.2s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['3.04.5', '10.0.00']

```
r'^\d+\.\d+\.\d+$'
```

## Attempt 2: FAIL (hidden: regex '^[1-9]\\d*\\.\\d+\\.\\d+$'; wrong on ['0.0.0', '!1.02.3', '!1.2.03'])

- 20 tokens in 4.2s, finish: stop
- verifier: FAIL: it does not match these, which it should: ['0.10.0']; it matches these, which it must reject: ['3.04.5', '10.0.00']

```
r'^[1-9]\d*\.\d+\.\d+$'
```

## Attempt 3: FAIL (hidden: regex '^[1-9]\\d*\\.\\d*\\.\\d+$'; wrong on ['0.0.0', '!1.02.3', '!1.2.03'])

- 20 tokens in 5.5s, finish: stop
- verifier: FAIL: it does not match these, which it should: ['0.10.0']; it matches these, which it must reject: ['3.04.5', '10.0.00']

```
r'^[1-9]\d*\.\d*\.\d+$'
```
