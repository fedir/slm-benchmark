# nemotron-3-nano-4b / regex-mac / seed 45 / harness

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a MAC address: six pairs of hex digits (either case) separated by colons. Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: PASS (hidden: regex '^(?:[0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}$')

- 31 tokens in 7.1s, finish: stop
- verifier: pass

```python
^(?:[0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}$
```
