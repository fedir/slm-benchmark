# qwen2.5-coder-3b / regex-slug / seed 46 / resample (no feedback)

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a URL slug: lowercase letters and digits in words separated by single hyphens, with no leading, trailing or doubled hyphen. Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: regex '^[-\\w]+$'; wrong on ['!Hello', '!hello_world', '!-hello', '!hello-', '!hello--world'])

- 10 tokens in 2.5s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['My-Post', 'post-', 'a--b']

```
^[-\w]+$
```

## Attempt 2: PASS (hidden: regex '^[a-z0-9]+(-[a-z0-9]+)*$')

- 21 tokens in 3.4s, finish: stop
- verifier: pass

```
^[a-z0-9]+(-[a-z0-9]+)*$
```
