# nemotron-3-nano-4b / regex-uuid / seed 45 / resample (no feedback)

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a UUID in canonical form: 8-4-4-4-12 LOWERCASE hex digits separated by hyphens. Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: regex '^\\(?([0-9a-f]{4})-(?=[0-9a-f]{4})-(?=[0-9a-f]{4})-(?=[0-9a-f]{4})-(?=[0-9a-f]{12})[0-9a-f]{12}\\)?$`'; wrong on ['123e4567-e89b-12d3-a456-426614174000', '00000000-0000-0000-0000-000000000000', 'ffffffff-ffff-ffff-ffff-ffffffffffff'])

- 75 tokens in 13.4s, finish: stop
- verifier: FAIL: it does not match these, which it should: ['550e8400-e29b-41d4-a716-446655440000', 'aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee']

```python
^\(?([0-9a-f]{4})-(?=[0-9a-f]{4})-(?=[0-9a-f]{4})-(?=[0-9a-f]{4})-(?=[0-9a-f]{12})[0-9a-f]{12}\)?$`
```

## Attempt 2: PASS (hidden: regex '^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')

- 54 tokens in 10.1s, finish: stop
- verifier: pass

```python
r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
```
