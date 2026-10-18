# ornith-9b-mtp / regex-time24 / seed 45 / harness

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a 24-hour clock time `HH:MM` with two-digit hours 00-23 and two-digit minutes 00-59. Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: PASS (hidden: regex '^(?:(?:[01]\\d|2[0-3]):[0-5]\\d)$')

- 28 tokens in 10.6s, finish: stop
- verifier: pass

```
^(?:(?:[01]\d|2[0-3]):[0-5]\d)$
```
