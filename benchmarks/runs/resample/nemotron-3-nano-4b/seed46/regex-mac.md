# nemotron-3-nano-4b / regex-mac / seed 46 / resample (no feedback)

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a MAC address: six pairs of hex digits (either case) separated by colons. Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: PASS (hidden: regex '^[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}$')

- 33 tokens in 6.6s, finish: stop
- verifier: pass

```python
r'^[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}$'
```
