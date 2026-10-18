# nemotron-3-nano-4b / py-editdist / seed 46 / resample (no feedback)

## Prompt

Write a Python function `edit_distance(a, b)` returning the Levenshtein edit distance between two strings (insert, delete, replace, each cost 1). It is tested on strings of 1500 characters. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 169 tokens in 25.5s, finish: stop
- verifier: pass

```python
def edit_distance(a, b):
    if len(a) == 0:
        return len(b)
    if len(b) == 0:
        return len(a)
    prev = [i for i in range(len(a) + 1)]
    for j in range(1, len(b) + 1):
        curr = [0] * (len(a) + 1)
        curr[0] = j
        for i in range(1, len(a) + 1):
            if a[i-1] == b[j-1]:
                curr[i] = prev[i-1]
            else:
                curr[i] = min(prev[i-1], prev[i], curr[i-1]) + 1
        prev = curr
    return prev[-1]
```
