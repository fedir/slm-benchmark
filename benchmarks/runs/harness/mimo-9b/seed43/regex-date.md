# mimo-9b / regex-date / seed 43 / harness

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches dates in the format YYYY-MM-DD where the month is 01-12 and the day is 01-31 (no need to check month lengths). Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: regex '^\\d{4}-(0[1-9]|[12]\\d|3[01])-(0[1-9]|[12]\\d|3[01])$'; wrong on ['!2024-13-01'])

- 45 tokens in 15.5s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['2023-15-10']

```
^\d{4}-(0[1-9]|[12]\d|3[01])-(0[1-9]|[12]\d|3[01])$
```

## Attempt 2: FAIL (hidden: regex '^\\d{4}-(0[1-9]|[12]\\d|3[01])-(0[1-9]|[12]\\d|3[01])$'; wrong on ['!2024-13-01'])

- 512 tokens in 140.6s, finish: length
- verifier: FAIL: it matches these, which it must reject: ['2023-15-10']

```
^\d{4}-(0[1-9]|[12]\d|3[01])-(0[1-9]|[12]\d|3[01])$
```

Wait — `15` is already rejected by `3[01]`. Let me re-check: `0[1-9]` matches 01-09, `[12]\d` matches 10-29, `3[01]` matches 30-31. So 15 would match `[12]\d` (15). The issue is that this regex allows 10-29 for days, but 31 is allowed too — 15 is valid per the spec (day is 01-31).

The correct regex should be:
```
^\d{4}-(0[1-9]|[12]\d|3[01])-(0[1-9]|[12]\d|3[01])$
```

Wait, the day part: 01-31. `0[1-9]` = 01-09, `[12]\d` = 10-29, `3[01]` = 30-31. That's 01-31. So 15 is correctly matched as a day.

The original regex is actually correct for the requirements. The verification claim that 15-10 should be rejected contradicts the stated spec (day 01-31).

Hmm, but the user says it fails verification because it matches 2023-15-10 which "must reject". But per the spec, day 15 is valid (01-31). Unless there's additional context... Let me just re-read.

The spec says "the day is 01-31 (no need to check month lengths)". So 2023-15-10 has month 15, which should be rejected. Let me check: month part is `(0[1-9]|[12]\d|3[01])`. For 15: `0[1-9]` no (15 starts with 1), `[12]\d` yes (1 matches [12], 5 matches \d). So 

## Attempt 3: PASS (hidden: regex '^\\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\d|3[01])$')

- 41 tokens in 34.8s, finish: stop
- verifier: pass

```
^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$
```
