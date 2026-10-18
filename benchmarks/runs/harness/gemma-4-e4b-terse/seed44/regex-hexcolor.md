# gemma-4-e4b-terse / regex-hexcolor / seed 44 / harness

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a CSS hex color: '#' followed by exactly 3 or exactly 6 hex digits (case-insensitive). Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: regex '^#([0-9a-f]{3}|[0-9a-f]{6})$'; wrong on ['#A1b2C3', '#1aF'])

- 28 tokens in 7.7s, finish: stop
- verifier: FAIL: it does not match these, which it should: ['#DEF012', '#9a8B7c']

```regex
^#([0-9a-f]{3}|[0-9a-f]{6})$
```

## Attempt 2: PASS (hidden: regex '^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$')

- 34 tokens in 11.0s, finish: stop
- verifier: pass

```regex
^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$
```
