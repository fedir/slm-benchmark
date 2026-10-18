# gemma-4-e4b-concise / py-spiral / seed 42 / harness

## Prompt

Write a Python function `spiral_order(matrix)` returning the elements of a rectangular matrix (list of lists) in clockwise spiral order starting at the top-left, e.g. [[1,2],[3,4]] gives [1,2,4,3]. An empty matrix gives []. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 270 tokens in 44.5s, finish: stop
- verifier: pass

```python
def spiral_order(matrix):
    if not matrix:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    top, bottom, left, right = 0, rows - 1, 0, cols - 1
    result = []
    while top <= bottom and left <= right:
        # Traverse right
        for c in range(left, right + 1):
            result.append(matrix[top][c])
        top += 1
        if top > bottom:
            break

        # Traverse down
        for r in range(top, bottom + 1):
            result.append(matrix[r][right])
        right -= 1
        if left > right:
            break

        # Traverse left
        for c in range(right, left - 1, -1):
            result.append(matrix[bottom][c])
        bottom -= 1
        if top > bottom:
            break

        # Traverse up
        for r in range(bottom, top - 1, -1):
            result.append(matrix[r][left])
        left += 1
    return result
```
