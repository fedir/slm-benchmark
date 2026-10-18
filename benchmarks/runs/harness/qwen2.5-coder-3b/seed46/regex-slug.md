# qwen2.5-coder-3b / regex-slug / seed 46 / harness

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a URL slug: lowercase letters and digits in words separated by single hyphens, with no leading, trailing or doubled hyphen. Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: regex '^[-\\w]+$'; wrong on ['!Hello', '!hello_world', '!-hello', '!hello-', '!hello--world'])

- 10 tokens in 2.5s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['My-Post', 'post-', 'a--b']

```
^[-\w]+$
```

## Attempt 2: FAIL (hidden: regex '^(?!-*-*)([a-z0-9]+(-[a-z0-9]+)*)$'; wrong on ['hello', 'hello-world', 'a1-b2-c3', '2024-report', 'x'])

- 27 tokens in 4.6s, finish: stop
- verifier: FAIL: it does not match these, which it should: ['my-first-post', 'v2', 'a-b-c']

```
^(?!-*-*)([a-z0-9]+(-[a-z0-9]+)*)$
```

## Attempt 3: FAIL (hidden: regex '^[-a-z0-9]+$'; wrong on ['!-hello', '!hello-', '!hello--world'])

- 13 tokens in 4.0s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['post-', 'a--b']

```
^[-a-z0-9]+$
```
