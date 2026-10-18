# mimo-9b / regex-hexcolor / seed 43 / harness

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a CSS hex color: '#' followed by exactly 3 or exactly 6 hex digits (case-insensitive). Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: regex '^#(?:(?:[0-9a-f]{3})|(?:[0-9a-f]{6}))$'; wrong on ['#A1b2C3', '#1aF'])

- 31 tokens in 10.8s, finish: stop
- verifier: FAIL: it does not match these, which it should: ['#DEF012', '#9a8B7c']

```
^#(?:(?:[0-9a-f]{3})|(?:[0-9a-f]{6}))$
```

## Attempt 2: PASS (hidden: regex '^#(?i:[0-9a-f]{3}|[0-9a-f]{6})$')

- 28 tokens in 15.1s, finish: stop
- verifier: pass

```
^#(?i:[0-9a-f]{3}|[0-9a-f]{6})$
```
