# ornith-9b-mtp / regex-date

- category: regex
- result: **PASS** (regex '\\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])')
- tokens: 42 in 14s (3.1 t/s), finish: stop

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches dates in the format YYYY-MM-DD where the month is 01-12 and the day is 01-31 (no need to check month lengths). Reply with ONLY the regex in a code block, no explanation.

## Answer

```regex
\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])
```
