# ornith-9b-mtp / regex-hexcolor / seed 46 / harness

## Prompt

Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches a CSS hex color: '#' followed by exactly 3 or exactly 6 hex digits (case-insensitive). Reply with ONLY the regex in a code block, no explanation.

## Attempt 1: FAIL (hidden: regex '^#[0-9a-fA-F]{3,6}$'; wrong on ['!#ffff', '!#12345'])

- 20 tokens in 8.5s, finish: stop
- verifier: FAIL: it matches these, which it must reject: ['#abcd']

```regex
^#[0-9a-fA-F]{3,6}$
```

## Attempt 2: FAIL (hidden: regex '^#[0-9a-fA-F]{3}|\\^#[0-9a-fA-F]{6}$'; wrong on ['#A1b2C3', '#000000'])

- 31 tokens in 12.4s, finish: stop
- verifier: FAIL: it does not match these, which it should: ['#DEF012', '#9a8B7c']

```regex
^#[0-9a-fA-F]{3}|\^#[0-9a-fA-F]{6}$
```

## Attempt 3: PASS (hidden: regex '^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$')

- 31 tokens in 16.2s, finish: stop
- verifier: pass

```regex
^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$
```
