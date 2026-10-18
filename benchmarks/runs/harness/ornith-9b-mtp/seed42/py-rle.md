# ornith-9b-mtp / py-rle / seed 42 / harness

## Prompt

Write a Python function `rle_encode(s)` that run-length encodes a string: each run of identical characters becomes the character followed by the run length, e.g. 'aaabcc' becomes 'a3b1c2'. The empty string gives ''. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 109 tokens in 22.4s, finish: stop
- verifier: pass

```python
def rle_encode(s):
    if not s:
        return ''
    encoded = []
    prev_char = s[0]
    count = 1
    for char in s[1:]:
        if char == prev_char:
            count += 1
        else:
            encoded.append(prev_char + str(count))
            prev_char = char
            count = 1
    encoded.append(prev_char + str(count))
    return ''.join(encoded)
```
