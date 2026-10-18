# ornith-9b-mtp / py-rle / seed 45 / resample (no feedback)

## Prompt

Write a Python function `rle_encode(s)` that run-length encodes a string: each run of identical characters becomes the character followed by the run length, e.g. 'aaabcc' becomes 'a3b1c2'. The empty string gives ''. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: TypeError: can't multiply sequence by non-int of type 'itertools._grouper')

- 35 tokens in 10.8s, finish: stop
- verifier: FAIL: rle_encode('wwwwb') raised TypeError: can't multiply sequence by non-int of type 'itertools._grouper'; rle_encode('abc') raised TypeError: can't multiply sequence by non-int of type 'itertools._grouper'

```python
def rle_encode(s):
    return ''.join(c * n for c, n in __import__('itertools').groupby(s))
```

## Attempt 2: PASS (hidden: tests passed)

- 104 tokens in 21.1s, finish: stop
- verifier: pass

```python
def rle_encode(s):
    if not s:
        return ''
    encoded = []
    prev = s[0]
    count = 1
    for char in s[1:]:
        if char == prev:
            count += 1
        else:
            encoded.append(prev + str(count))
            prev = char
            count = 1
    encoded.append(prev + str(count))
    return ''.join(encoded)
```
