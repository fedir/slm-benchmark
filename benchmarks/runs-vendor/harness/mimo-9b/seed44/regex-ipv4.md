# mimo-9b / regex-ipv4 / seed 44 / harness

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a valid IPv4 address: four decimal numbers 0-255 separated by dots. Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: regex '^(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?){4}$'; wrong on ['192.168.1.1', '0.0.0.0', '255.255.255.255', '10.0.42.7'])

- 40 tokens in 12.9s, finish: stop
- verifier: FAIL: it does not match these, which it should: ['8.8.8.8', '127.0.0.1', '172.16.254.1']

```
^(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?){4}$
```

## Attempt 2: FAIL (hidden: regex '^(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?){4}$'; wrong on ['192.168.1.1', '0.0.0.0', '255.255.255.255', '10.0.42.7'])

- 39 tokens in 20.1s, finish: stop
- verifier: FAIL: it does not match these, which it should: ['8.8.8.8', '127.0.0.1', '172.16.254.1']

```
^(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?){4}$
```

## Attempt 3: FAIL (hidden: regex '^(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?){4}$'; wrong on ['192.168.1.1', '0.0.0.0', '255.255.255.255', '10.0.42.7'])

- 39 tokens in 22.4s, finish: stop
- verifier: FAIL: it does not match these, which it should: ['8.8.8.8', '127.0.0.1', '172.16.254.1']

```
^(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?){4}$
```
