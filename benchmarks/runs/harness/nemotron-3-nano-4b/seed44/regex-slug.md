# nemotron-3-nano-4b / regex-slug / seed 44 / harness

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a URL slug: lowercase letters and digits in words separated by single hyphens, with no leading, trailing or doubled hyphen. Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: regex '^[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$'; wrong on ['!hello--world'])

- 30 tokens in 6.8s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['a--b']

```python
^[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$```

## Attempt 2: FAIL (hidden: regex '^[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$'; wrong on ['!hello--world'])

- 30 tokens in 8.1s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['a--b']

```python
^[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$```

## Attempt 3: FAIL (hidden: regex '^[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$'; wrong on ['!hello--world'])

- 30 tokens in 10.4s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['a--b']

```python
^[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$```
