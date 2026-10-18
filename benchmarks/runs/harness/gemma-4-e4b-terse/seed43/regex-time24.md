# gemma-4-e4b-terse / regex-time24 / seed 43 / harness

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a 24-hour clock time `HH:MM` with two-digit hours 00-23 and two-digit minutes 00-59. Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: PASS (hidden: regex '^(?:[01]\\d|2[0-3]):[0-5]\\d$')

- 27 tokens in 8.1s, finish: stop
- verifier: pass

```regex
^(?:[01]\d|2[0-3]):[0-5]\d$
```
