# qwen2.5-coder-3b / regex-uuid / seed 44 / harness

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a UUID in canonical form: 8-4-4-4-12 LOWERCASE hex digits separated by hyphens. Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: regex '^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$'; wrong on ['!123E4567-e89b-12d3-a456-426614174000'])

- 61 tokens in 7.6s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['550E8400-e29b-41d4-a716-446655440000']

```
^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
```

## Attempt 2: PASS (hidden: regex '^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')

- 51 tokens in 7.9s, finish: stop
- verifier: pass

```
^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
```
