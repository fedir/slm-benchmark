# qwen2.5-coder-3b / regex-ipv4 / seed 42 / harness

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a valid IPv4 address: four decimal numbers 0-255 separated by dots. Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: regex '^(\\d{1,3}\\.){3}\\d{1,3}$'; wrong on ['!256.1.1.1', '!300.1.1.1'])

- 25 tokens in 4.1s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['999.1.1.1']

```python
r'^(\d{1,3}\.){3}\d{1,3}$'
```

## Attempt 2: FAIL (hidden: regex '^(\\d{1,3}\\.){3}\\d{1,2}$'; wrong on ['255.255.255.255', '!256.1.1.1', '!300.1.1.1'])

- 25 tokens in 4.6s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['999.1.1.1']

```python
r'^(\d{1,3}\.){3}\d{1,2}$'
```

## Attempt 3: FAIL (hidden: regex '^(\\d{1,3}\\.){3}([0-9]|[1-9]\\d|1\\d\\d|2[0-4]\\d|25[0-5])$'; wrong on ['!256.1.1.1', '!300.1.1.1'])

- 50 tokens in 7.5s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['999.1.1.1']

```python
r'^(\d{1,3}\.){3}([0-9]|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])$'
```
