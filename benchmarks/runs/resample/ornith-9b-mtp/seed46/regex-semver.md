# ornith-9b-mtp / regex-semver / seed 46 / resample (no feedback)

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a version `MAJOR.MINOR.PATCH` where each part is a non-negative integer without leading zeros (so `0` is allowed, `01` is not). Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: regex '^(?:(?:0|[1-9][0-9]*)\\.)+(?:0|[1-9][0-9]*)$'; wrong on ['!1.2', '!1.2.3.4'])

- 35 tokens in 11.9s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['4.5', '1.2.3.4.5']

```regex
^(?:(?:0|[1-9][0-9]*)\.)+(?:0|[1-9][0-9]*)$
```

## Attempt 2: PASS (hidden: regex '^(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)$')

- 42 tokens in 11.8s, finish: stop
- verifier: pass

```regex
^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$
```
