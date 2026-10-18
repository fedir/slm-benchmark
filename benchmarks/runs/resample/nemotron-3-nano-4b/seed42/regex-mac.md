# nemotron-3-nano-4b / regex-mac / seed 42 / resample (no feedback)

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a MAC address: six pairs of hex digits (either case) separated by colons. Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: PASS (hidden: regex '\\b([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}\\b')

- 31 tokens in 6.3s, finish: stop
- verifier: pass

```
\b([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}\b
```
