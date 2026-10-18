# gemma-4-e4b-terse / regex-time24 / seed 45 / harness

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a 24-hour clock time `HH:MM` with two-digit hours 00-23 and two-digit minutes 00-59. Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: regex '(2[0-3]|[01]?[0-9]):([0-5][0-9])'; wrong on ['!9:05'])

- 30 tokens in 8.5s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['1:15']

```regex
(2[0-3]|[01]?[0-9]):([0-5][0-9])
```

## Attempt 2: PASS (hidden: regex '(2[0-3]|[01][0-9]):([0-5][0-9])')

- 29 tokens in 10.1s, finish: stop
- verifier: pass

```regex
(2[0-3]|[01][0-9]):([0-5][0-9])
```
