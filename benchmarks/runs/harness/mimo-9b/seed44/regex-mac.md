# mimo-9b / regex-mac / seed 44 / harness

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a MAC address: six pairs of hex digits (either case) separated by colons. Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: PASS (hidden: regex '^[0-9a-fA-F]{2}:([0-9a-fA-F]{2}:){4}[0-9a-fA-F]{2}$')

- 40 tokens in 14.0s, finish: stop
- verifier: pass

```
^[0-9a-fA-F]{2}:([0-9a-fA-F]{2}:){4}[0-9a-fA-F]{2}$
```
