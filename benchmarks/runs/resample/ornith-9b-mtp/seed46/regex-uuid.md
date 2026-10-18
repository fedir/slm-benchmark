# ornith-9b-mtp / regex-uuid / seed 46 / resample (no feedback)

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a UUID in canonical form: 8-4-4-4-12 LOWERCASE hex digits separated by hyphens. Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: PASS (hidden: regex '^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')

- 52 tokens in 13.6s, finish: stop
- verifier: pass

```regex
^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
