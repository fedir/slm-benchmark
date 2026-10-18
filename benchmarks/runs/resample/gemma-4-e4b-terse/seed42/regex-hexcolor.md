# gemma-4-e4b-terse / regex-hexcolor / seed 42 / resample (no feedback)

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a CSS hex color: '#' followed by exactly 3 or exactly 6 hex digits (case-insensitive). Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: PASS (hidden: regex '^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$')

- 34 tokens in 8.9s, finish: stop
- verifier: pass

```regex
^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$
```
