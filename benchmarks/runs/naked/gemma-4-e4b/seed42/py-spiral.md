# gemma-4-e4b / py-spiral / seed 42 / naked

## Prompt

Write a Python function `spiral_order(matrix)` returning the elements of a rectangular matrix (list of lists) in clockwise spiral order starting at the top-left, e.g. [[1,2],[3,4]] gives [1,2,4,3]. An empty matrix gives []. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 325 tokens in 49.7s, finish: stop

```python
def spiral_order(matrix):
    """
    Returns the elements of a rectangular matrix (list of lists) in clockwise spiral order 
    starting at the top-left.
    """
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    result = []

    top, bottom, left, right = 0, rows - 1, 0, cols - 1

    while top <= bottom and left <= right:
        # Traverse Right (Top row)
        for c in range(left, right + 1):
            result.append(matrix[top][c])
        top += 1

        if top > bottom:
            break

        # Traverse Down (Right column)
        for r in range(top, bottom + 1):
            result.append(matrix[r][right])
        right -= 1

        if left > right:
            break

        # Traverse Left (Bottom row)
        for c in range(right, left - 1, -1):
            result.append(matrix[bottom][c])
        bottom -= 1

        if top > bottom:
            break

        # Traverse Up (Left column)
        for r in range(bottom, top - 1, -1):
            result.append(matrix[r][left])
        left += 1

    return result
```
