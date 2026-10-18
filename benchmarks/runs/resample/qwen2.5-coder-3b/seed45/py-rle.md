# qwen2.5-coder-3b / py-rle / seed 45 / resample (no feedback)

## Prompt

Write a Python function `rle_encode(s)` that run-length encodes a string: each run of identical characters becomes the character followed by the run length, e.g. 'aaabcc' becomes 'a3b1c2'. The empty string gives ''. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 104 tokens in 10.6s, finish: stop
- verifier: pass

```python
def rle_encode(s):
    if not s:
        return ''
    
    encoded = ''
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded += s[i - 1] + str(count)
            count = 1
    
    # Add the last run
    encoded += s[-1] + str(count)
    
    return encoded
```
