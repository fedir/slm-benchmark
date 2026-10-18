# qwen2.5-coder-7b / regex-time24 / seed 45 / harness

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a 24-hour clock time `HH:MM` with two-digit hours 00-23 and two-digit minutes 00-59. Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: regex '^\\d{2}:\\d{2}$'; wrong on ['!24:00', '!12:60'])

- 16 tokens in 6.5s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['25:10', '10:75']

```python
^\d{2}:\d{2}$
```

## Attempt 2: PASS (hidden: regex '^(?:[01]\\d|2[0-3]):(?:[0-5]\\d)$')

- 28 tokens in 10.2s, finish: stop
- verifier: pass

```python
^(?:[01]\d|2[0-3]):(?:[0-5]\d)$
```
