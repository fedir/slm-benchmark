# ornith-9b-mtp / py-rle / seed 43 / resample (no feedback)

## Prompt

Write a Python function `rle_encode(s)` that run-length encodes a string: each run of identical characters becomes the character followed by the run length, e.g. 'aaabcc' becomes 'a3b1c2'. The empty string gives ''. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: AssertionError)

- 102 tokens in 21.3s, finish: stop
- verifier: FAIL: rle_encode('wwwwb') raised TypeError: can only concatenate str (not "int") to str; rle_encode('abc') returned 'abc', expected 'a1b1c1'

```python
def rle_encode(s):
    if not s:
        return ''
    encoded = []
    for char in s:
        if encoded and encoded[-1][0] == char:
            count, _ = encoded[-1]
            encoded[-1] = (char, count + 1)
        else:
            encoded.append((char, 1))
    return ''.join(char * count for char, count in encoded)
```

## Attempt 2: PASS (hidden: tests passed)

- 110 tokens in 22.6s, finish: stop
- verifier: pass

```python
def rle_encode(s):
    if not s:
        return ''
    encoded = []
    char = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == char:
            count += 1
        else:
            encoded.append(char + str(count))
            char = s[i]
            count = 1
    encoded.append(char + str(count))
    return ''.join(encoded)
```
