# ornith-9b-mtp / regex-mac / seed 46 / resample (no feedback)

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a MAC address: six pairs of hex digits (either case) separated by colons. Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: PASS (hidden: regex '^([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}$')

- 30 tokens in 8.4s, finish: stop
- verifier: pass

```
^([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}$
```
