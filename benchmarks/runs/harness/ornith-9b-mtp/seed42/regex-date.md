# ornith-9b-mtp / regex-date / seed 42 / harness

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches dates in the format YYYY-MM-DD where the month is 01-12 and the day is 01-31 (no need to check month lengths). Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: PASS (hidden: regex '\\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])')

- 42 tokens in 12.9s, finish: stop
- verifier: pass

```regex
\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])
```
