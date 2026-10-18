# mimo-9b / regex-mac / seed 43 / harness

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a MAC address: six pairs of hex digits (either case) separated by colons. Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: PASS (hidden: regex '^([0-9A-Fa-f]{2})[:]([0-9A-Fa-f]{2})[:]([0-9A-Fa-f]{2})[:]([0-9A-Fa-f]{2})[:]([0-9A-Fa-f]{2})[:]([0-9A-Fa-f]{2})$')

- 83 tokens in 24.5s, finish: stop
- verifier: pass

```
^([0-9A-Fa-f]{2})[:]([0-9A-Fa-f]{2})[:]([0-9A-Fa-f]{2})[:]([0-9A-Fa-f]{2})[:]([0-9A-Fa-f]{2})[:]([0-9A-Fa-f]{2})$
```
