# gemma-4-e4b-terse / regex-slug / seed 46 / harness

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a URL slug: lowercase letters and digits in words separated by single hyphens, with no leading, trailing or doubled hyphen. Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: PASS (hidden: regex '^[a-z0-9]+(-[a-z0-9]+)*$')

- 25 tokens in 7.8s, finish: stop
- verifier: pass

```regex
^[a-z0-9]+(-[a-z0-9]+)*$
```
