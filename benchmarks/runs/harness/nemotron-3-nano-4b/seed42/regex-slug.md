# nemotron-3-nano-4b / regex-slug / seed 42 / harness

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a URL slug: lowercase letters and digits in words separated by single hyphens, with no leading, trailing or doubled hyphen. Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: regex '^[a-z0-9](?:-[a-z0-9]+)*$'; wrong on ['hello', 'hello-world', 'a1-b2-c3', '2024-report'])

- 22 tokens in 5.7s, finish: stop
- verifier: FAIL: it does not match these, which it should: ['my-first-post', 'v2']

```python
^[a-z0-9](?:-[a-z0-9]+)*$
```

## Attempt 2: FAIL (hidden: regex '^[a-z0-9](?:-[a-z0-9]+)*$'; wrong on ['hello', 'hello-world', 'a1-b2-c3', '2024-report'])

- 22 tokens in 7.0s, finish: stop
- verifier: FAIL: it does not match these, which it should: ['my-first-post', 'v2']

```python
^[a-z0-9](?:-[a-z0-9]+)*$
```

## Attempt 3: FAIL (hidden: regex '^[a-z0-9](?:-[a-z0-9]+)*$'; wrong on ['hello', 'hello-world', 'a1-b2-c3', '2024-report'])

- 22 tokens in 9.1s, finish: stop
- verifier: FAIL: it does not match these, which it should: ['my-first-post', 'v2']

```python
^[a-z0-9](?:-[a-z0-9]+)*$
```
