# nemotron-3-nano-4b / regex-ipv4 / seed 42 / harness

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a valid IPv4 address: four decimal numbers 0-255 separated by dots. Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: PASS (hidden: regex '^(?:(?:25[0-5]|2[0-4]\\d|[01]?\\d\\d?)\\.){3}(?:25[0-5]|2[0-4]\\d|[01]?\\d\\d?)$')

- 65 tokens in 10.9s, finish: stop
- verifier: pass

```python
^(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)$
```
