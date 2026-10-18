# ornith-9b-mtp / regex-hexcolor

- category: regex
- result: **PASS** (regex '^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$')
- tokens: 32 in 11s (3.0 t/s), finish: stop

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a CSS hex color: '#' followed by exactly 3 or exactly 6 hex digits (case-insensitive). Reply with ONLY the regex in a code block, no explanation.

## Answer

```regex
^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$
```
