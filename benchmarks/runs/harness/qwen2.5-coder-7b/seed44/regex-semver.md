# qwen2.5-coder-7b / regex-semver / seed 44 / harness

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a version `MAJOR.MINOR.PATCH` where each part is a non-negative integer without leading zeros (so `0` is allowed, `01` is not). Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: regex '^\\d+\\.\\d+\\.\\d+$'; wrong on ['!01.2.3', '!1.02.3', '!1.2.03'])

- 15 tokens in 6.3s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['3.04.5', '10.0.00']

```python
^\d+\.\d+\.\d+$
```

## Attempt 2: FAIL (hidden: regex '^\\d+(?:\\.\\d+){2}$'; wrong on ['!01.2.3', '!1.02.3', '!1.2.03'])

- 17 tokens in 8.2s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['3.04.5', '10.0.00']

```python
^\d+(?:\.\d+){2}$
```

## Attempt 3: FAIL (hidden: regex '^\\d+(?:\\.(?:0|[1-9]\\d*)){2}$'; wrong on ['!01.2.3'])

- 24 tokens in 10.7s, finish: stop
- verifier: pass

```python
^\d+(?:\.(?:0|[1-9]\d*)){2}$
```
