# nemotron-3-nano-4b / py-editdist / seed 42 / resample (no feedback)

## Prompt

Write a Python function `edit_distance(a, b)` returning the Levenshtein edit distance between two strings (insert, delete, replace, each cost 1). It is tested on strings of 1500 characters. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: IndexError: list index out of range)

- 172 tokens in 25.9s, finish: stop
- verifier: pass

```python
def edit_distance(a, b):
    if not a: return len(b)
    if not b: return len(a)
    m, n = len(a), len(b)
    prev = [i for i in range(m + 1)]
    curr = [0] * (m + 1)
    for i in range(1, m + 1):
        curr[0] = i
        for j in range(1, n + 1):
            if a[i-1] == b[j-1]:
                curr[j] = prev[j-1]
            else:
                curr[j] = 1 + min(prev[j], curr[j-1], prev[j-1])
        prev, curr = curr, [0] * (m + 1)
    return prev[n]
```
