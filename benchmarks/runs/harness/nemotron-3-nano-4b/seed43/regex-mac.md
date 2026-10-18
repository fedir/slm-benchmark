# nemotron-3-nano-4b / regex-mac / seed 43 / harness

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a MAC address: six pairs of hex digits (either case) separated by colons. Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: regex '^[0-9a-fA-F:]+$'; wrong on ['!00:1A:2b:3C:4d', '!00:1A:2b:3C:4d:5E:6F', '!0:1A:2b:3C:4d:5E'])

- 19 tokens in 4.6s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['12:34:56:78:9A']

```python
r'^[0-9a-fA-F:]+$'
```

## Attempt 2: PASS (hidden: regex '^[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}$')

- 74 tokens in 14.2s, finish: stop
- verifier: pass

```python
r'^[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}$'
```
