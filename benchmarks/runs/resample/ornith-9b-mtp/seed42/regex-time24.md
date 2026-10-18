# ornith-9b-mtp / regex-time24 / seed 42 / resample (no feedback)

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a 24-hour clock time `HH:MM` with two-digit hours 00-23 and two-digit minutes 00-59. Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: PASS (hidden: regex '^([01][0-9]|2[0-3]):[0-5][0-9]$')

- 30 tokens in 10.6s, finish: stop
- verifier: pass

```regex
^([01][0-9]|2[0-3]):[0-5][0-9]$
```
