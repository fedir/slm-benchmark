# nemotron-3-nano-4b / regex-date

- category: regex
- result: **FAIL** (regex '\\b\\d{4}-\\d{2}-\\d{2}\\b'; wrong on ['!2024-13-01', '!2024-00-10', '!2024-01-32', '!2024-01-00'])
- tokens: 19 in 5s (3.7 t/s), finish: stop

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches dates in the format YYYY-MM-DD where the month is 01-12 and the day is 01-31 (no need to check month lengths). Reply with ONLY the regex in a code block, no explanation.

## Answer

```
\b\d{4}-\d{2}-\d{2}\b
```
