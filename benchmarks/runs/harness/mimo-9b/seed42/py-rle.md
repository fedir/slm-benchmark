# mimo-9b / py-rle / seed 42 / harness

## Prompt

Write a Python function `rle_encode(s)` that run-length encodes a string: each run of identical characters becomes the character followed by the run length, e.g. 'aaabcc' becomes 'a3b1c2'. The empty string gives ''. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 114 tokens in 33.2s, finish: stop
- verifier: pass

```python
def rle_encode(s):
    if not s:
        return ""

    result = []
    current_char = s[0]
    run_length = 1

    for char in s[1:]:
        if char == current_char:
            run_length += 1
        else:
            result.append(current_char + str(run_length))
            current_char = char
            run_length = 1

    result.append(current_char + str(run_length))
    return "".join(result)
```
