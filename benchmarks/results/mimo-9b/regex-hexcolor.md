# mimo-9b / regex-hexcolor

- category: regex
- result: **PASS** (regex '^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$')
- tokens: 33 in 12s (2.8 t/s), finish: stop

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a CSS hex color: '#' followed by exactly 3 or exactly 6 hex digits (case-insensitive). Reply with ONLY the regex in a code block, no explanation.

## Answer


```regex
^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$
```
