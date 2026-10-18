# qwen2.5-coder-7b / py-rle / seed 43 / resample (no feedback)

## Prompt

Write a Python function `rle_encode(s)` that run-length encodes a string: each run of identical characters becomes the character followed by the run length, e.g. 'aaabcc' becomes 'a3b1c2'. The empty string gives ''. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 97 tokens in 22.2s, finish: stop
- verifier: pass

```python
def rle_encode(s):
    if not s:
        return ''
    encoded = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            encoded.append(f"{s[i-1]}{count}")
            count = 1
    encoded.append(f"{s[-1]}{count}")
    return ''.join(encoded)
```
