# nemotron-3-nano-4b / py-rle / seed 42 / resample (no feedback)

## Prompt

Write a Python function `rle_encode(s)` that run-length encodes a string: each run of identical characters becomes the character followed by the run length, e.g. 'aaabcc' becomes 'a3b1c2'. The empty string gives ''. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 87 tokens in 14.7s, finish: stop
- verifier: pass

```python
def rle_encode(s):
    if not s:
        return ''
    result = []
    i = 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]:
            j += 1
        result.append(f"{s[i]}{j - i}")
        i = j
    return ''.join(result)
```
