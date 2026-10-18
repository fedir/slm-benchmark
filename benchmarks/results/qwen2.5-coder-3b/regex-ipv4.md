# qwen2.5-coder-3b / regex-ipv4

- category: regex
- result: **FAIL** (regex '^(\\d{1,3}\\.){3}\\d{1,3}$'; wrong on ['!256.1.1.1', '!300.1.1.1'])
- tokens: 25 in 4s (6.3 t/s), finish: stop

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a valid IPv4 address: four decimal numbers 0-255 separated by dots. Reply with ONLY the regex in a code block, no explanation.

## Answer

```python
r'^(\d{1,3}\.){3}\d{1,3}$'
```
