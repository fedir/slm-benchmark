# mimo-9b / regex-semver / seed 42 / harness

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a version `MAJOR.MINOR.PATCH` where each part is a non-negative integer without leading zeros (so `0` is allowed, `01` is not). Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: regex '^[0-9]([0-9]*[0-9A-Fa-f])?([.][0-9]([0-9]*[0-9A-Fa-f])?){2}$'; wrong on ['!01.2.3', '!1.02.3', '!1.2.03'])

- 50 tokens in 18.2s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['3.04.5', '10.0.00']

```
^[0-9]([0-9]*[0-9A-Fa-f])?([.][0-9]([0-9]*[0-9A-Fa-f])?){2}$
```

## Attempt 2: FAIL (hidden: regex '^[0-9]([0-9]*[0-9A-Fa-f])?([.][0-9]([0-9]*[0-9A-Fa-f])?){2}$'; wrong on ['!01.2.3', '!1.02.3', '!1.2.03'])

- 50 tokens in 21.9s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['3.04.5', '10.0.00']

```
^[0-9]([0-9]*[0-9A-Fa-f])?([.][0-9]([0-9]*[0-9A-Fa-f])?){2}$
```

## Attempt 3: FAIL (hidden: regex '^[0-9]([0-9]*[0-9A-Fa-f])?([.][0-9]([0-9]*[0-9A-Fa-f])?){2}$'; wrong on ['!01.2.3', '!1.02.3', '!1.2.03'])

- 50 tokens in 26.2s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['3.04.5', '10.0.00']

```
^[0-9]([0-9]*[0-9A-Fa-f])?([.][0-9]([0-9]*[0-9A-Fa-f])?){2}$
```
