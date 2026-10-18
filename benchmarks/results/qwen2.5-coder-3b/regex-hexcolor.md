# qwen2.5-coder-3b / regex-hexcolor

- category: regex
- result: **FAIL** (regex '^#[0-9A-Fa-f]{3,6}$'; wrong on ['!#ffff', '!#12345'])
- tokens: 21 in 3s (7.0 t/s), finish: stop

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a CSS hex color: '#' followed by exactly 3 or exactly 6 hex digits (case-insensitive). Reply with ONLY the regex in a code block, no explanation.

## Answer

```python
r'^#[0-9A-Fa-f]{3,6}$'
```
