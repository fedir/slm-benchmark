# gemma-4-e4b-p-code-only / py-spiral / seed 43 / naked

## Prompt

Write a Python function `spiral_order(matrix)` returning the elements of a rectangular matrix (list of lists) in clockwise spiral order starting at the top-left, e.g. [[1,2],[3,4]] gives [1,2,4,3]. An empty matrix gives []. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 287 tokens in 45.9s, finish: stop

```python
def spiral_order(matrix):
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    result = []

    top, bottom = 0, rows - 1
    left, right = 0, cols - 1

    while top <= bottom and left <= right:
        # Traverse right (top row)
        for c in range(left, right + 1):
            result.append(matrix[top][c])
        top += 1

        if top > bottom:
            break

        # Traverse down (right column)
        for r in range(top, bottom + 1):
            result.append(matrix[r][right])
        right -= 1

        if left > right:
            break

        # Traverse left (bottom row)
        for c in range(right, left - 1, -1):
            result.append(matrix[bottom][c])
        bottom -= 1

        if top > bottom:
            break

        # Traverse up (left column)
        for r in range(bottom, top - 1, -1):
            result.append(matrix[r][left])
        left += 1

    return result
```
