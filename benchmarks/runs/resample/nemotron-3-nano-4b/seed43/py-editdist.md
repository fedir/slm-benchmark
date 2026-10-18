# nemotron-3-nano-4b / py-editdist / seed 43 / resample (no feedback)

## Prompt

Write a Python function `edit_distance(a, b)` returning the Levenshtein edit distance between two strings (insert, delete, replace, each cost 1). It is tested on strings of 1500 characters. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 185 tokens in 27.7s, finish: stop
- verifier: pass

```python
def edit_distance(a, b):
    m, n = len(a), len(b)
    prev = [0] * (n + 1)
    for j in range(n + 1):
        prev[j] = j
    for i in range(1, m + 1):
        curr = [0] * (n + 1)
        curr[0] = i
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                cost = 0
            else:
                cost = 1
            curr[j] = min(prev[j] + 1,      # deletion
                          curr[j - 1] + 1,   # insertion
                          prev[j - 1] + cost) # substitution
        prev = curr
    return prev[n]
```
