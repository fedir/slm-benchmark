# ornith-9b-mtp / py-rle / seed 44 / harness

## Prompt

Write a Python function `rle_encode(s)` that run-length encodes a string: each run of identical characters becomes the character followed by the run length, e.g. 'aaabcc' becomes 'a3b1c2'. The empty string gives ''. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: AssertionError)

- 99 tokens in 20.6s, finish: stop
- verifier: FAIL: rle_encode('abc') returned 'a1a1c1', expected 'a1b1c1'

```python
def rle_encode(s):
    if not s:
        return ''
    result = []
    count = 1
    for char in s[1:]:
        if char == s[0]:
            count += 1
        else:
            result.append(s[0] + str(count))
            count = 1
    result.append(s[-1] + str(count))
    return ''.join(result)
```

## Attempt 2: FAIL (hidden: AssertionError)

- 99 tokens in 24.2s, finish: stop
- verifier: FAIL: rle_encode('abc') returned 'a1a1c1', expected 'a1b1c1'

```python
def rle_encode(s):
    if not s:
        return ''
    result = []
    count = 1
    for char in s[1:]:
        if char == s[0]:
            count += 1
        else:
            result.append(s[0] + str(count))
            count = 1
    result.append(s[-1] + str(count))
    return ''.join(result)
```

## Attempt 3: FAIL (hidden: AssertionError)

- 99 tokens in 29.4s, finish: stop
- verifier: FAIL: rle_encode('wwwwb') returned 'w4w1', expected 'w4b1'; rle_encode('abc') returned 'a1a1a1', expected 'a1b1c1'

```python
def rle_encode(s):
    if not s:
        return ''
    result = []
    count = 1
    for char in s[1:]:
        if char == s[0]:
            count += 1
        else:
            result.append(s[0] + str(count))
            count = 1
    result.append(s[0] + str(count))
    return ''.join(result)
```
