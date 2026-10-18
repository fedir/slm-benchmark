# qwen2.5-coder-3b / regex-mac / seed 45 / resample (no feedback)

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a MAC address: six pairs of hex digits (either case) separated by colons. Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: PASS (hidden: regex '^[0-9A-Fa-f]{2}(:[0-9A-Fa-f]{2}){5}$')

- 32 tokens in 4.4s, finish: stop
- verifier: pass

```python
^[0-9A-Fa-f]{2}(:[0-9A-Fa-f]{2}){5}$
```
