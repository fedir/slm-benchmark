# gemma-4-e4b / regex-hexcolor / seed 42 / naked

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a CSS hex color: '#' followed by exactly 3 or exactly 6 hex digits (case-insensitive). Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: regex '^#([0-9a-f]{3}){1,2}$'; wrong on ['#A1b2C3', '#1aF'])

- 22 tokens in 5.1s, finish: stop

```regex
^#([0-9a-f]{3}){1,2}$
```
