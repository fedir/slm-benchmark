# mimo-9b / py-rle / seed 44 / harness

## Prompt

Write a Python function `rle_encode(s)` that run-length encodes a string: each run of identical characters becomes the character followed by the run length, e.g. 'aaabcc' becomes 'a3b1c2'. The empty string gives ''. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: no code block defining rle_encode(s))

- 127 tokens in 45.5s, finish: stop
- verifier: FAIL: no code block defining rle_encode(s)

```python
def rle_encode(s: str) -> str:
    if not s:
        return ""

    result = []
    current_char = s[0]
    run_length = 1

    for char in s[1:]:
        if char == current_char:
            run_length += 1
        else:
            result.append(current_char)
            result.append(str(run_length))
            current_char = char
            run_length = 1

    result.append(current_char)
    result.append(str(run_length))
    return "".join(result)
```

## Attempt 2: PASS (hidden: tests passed)

- 122 tokens in 57.1s, finish: stop
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
            result.append(current_char)
            result.append(str(run_length))
            current_char = char
            run_length = 1

    result.append(current_char)
    result.append(str(run_length))
    return "".join(result)
```
