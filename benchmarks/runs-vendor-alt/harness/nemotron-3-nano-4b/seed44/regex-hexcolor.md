# nemotron-3-nano-4b / regex-hexcolor / seed 44 / harness

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a CSS hex color: '#' followed by exactly 3 or exactly 6 hex digits (case-insensitive). Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: regex '#[0-9a-fA-F]{3,6}'; wrong on ['!#ffff', '!#12345'])

- 20 tokens in 6.2s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['#abcd']

```python
r'#[0-9a-fA-F]{3,6}'
```

## Attempt 2: PASS (hidden: regex '#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?$')

- 33 tokens in 9.3s, finish: stop
- verifier: pass

```python
r'#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?$'
```
