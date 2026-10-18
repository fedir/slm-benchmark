# nemotron-3-nano-4b / py-editdist / seed 44 / resample (no feedback)

## Prompt

Write a Python function `edit_distance(a, b)` returning the Levenshtein edit distance between two strings (insert, delete, replace, each cost 1). It is tested on strings of 1500 characters. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: AssertionError)

- 175 tokens in 26.3s, finish: stop
- verifier: FAIL: edit_distance('horse','ros') returned 0, expected 3; edit_distance('abc','xyz') returned 0, expected 3

```python
def edit_distance(a, b):
    if len(a) == 0:
        return len(b)
    if len(b) == 0:
        return len(a)
    if a == b:
        return 0
    n, m = len(a), len(b)
    prev = list(range(m + 1))
    for i in range(1, n + 1):
        curr = [i]
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                curr.append(min(prev[j], prev[j - 1], curr[-1] + 1))
            else:
                curr.append(min(prev[j], prev[j - 1], curr[-1] + 1))
        prev = curr
    return prev[-1]
```

## Attempt 2: PASS (hidden: tests passed)

- 151 tokens in 24.3s, finish: stop
- verifier: pass

```python
def edit_distance(a, b):
    m, n = len(a), len(b)
    if m == 0:
        return n
    if n == 0:
        return m
    prev = list(range(m + 1))
    for i in range(1, n + 1):
        curr = [i]
        for j in range(1, m + 1):
            if a[j-1] == b[i-1]:
                curr.append(min(prev[j], curr[j-1], prev[j-1]))
            else:
                curr.append(min(prev[j], curr[j-1], prev[j-1]) + 1)
        prev = curr
    return prev[m]
```
