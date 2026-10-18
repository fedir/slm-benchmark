# gemma-4-e4b / py-rle / seed 42 / naked

## Prompt

Write a Python function `rle_encode(s)` that run-length encodes a string: each run of identical characters becomes the character followed by the run length, e.g. 'aaabcc' becomes 'a3b1c2'. The empty string gives ''. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 126 tokens in 20.8s, finish: stop

```python
def rle_encode(s):
    if not s:
        return ""

    encoded = []
    i = 0
    n = len(s)

    while i < n:
        current_char = s[i]
        count = 0
        j = i
        while j < n and s[j] == current_char:
            count += 1
            j += 1

        encoded.append(current_char + str(count))
        i = j

    return "".join(encoded)
```
