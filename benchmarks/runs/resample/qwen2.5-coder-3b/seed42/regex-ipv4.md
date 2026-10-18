# qwen2.5-coder-3b / regex-ipv4 / seed 42 / resample (no feedback)

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a valid IPv4 address: four decimal numbers 0-255 separated by dots. Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: regex '^(\\d{1,3}\\.){3}\\d{1,3}$'; wrong on ['!256.1.1.1', '!300.1.1.1'])

- 25 tokens in 3.8s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['999.1.1.1']

```python
r'^(\d{1,3}\.){3}\d{1,3}$'
```

## Attempt 2: FAIL (hidden: regex '^\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}$'; wrong on ['!256.1.1.1', '!300.1.1.1'])

- 33 tokens in 4.6s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['999.1.1.1']

```
^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$
```

## Attempt 3: PASS (hidden: regex '\\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\b')

- 139 tokens in 13.9s, finish: stop
- verifier: pass

```python
\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b
```
