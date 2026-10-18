# ornith-9b-mtp / regex-mac / seed 44 / harness

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a MAC address: six pairs of hex digits (either case) separated by colons. Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: PASS (hidden: regex '^([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}$')

- 31 tokens in 8.8s, finish: stop
- verifier: pass

```regex
^([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}$
```
