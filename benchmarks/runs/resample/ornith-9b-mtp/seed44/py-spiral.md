# ornith-9b-mtp / py-spiral / seed 44 / resample (no feedback)

## Prompt

Write a Python function `spiral_order(matrix)` returning the elements of a rectangular matrix (list of lists) in clockwise spiral order starting at the top-left, e.g. [[1,2],[3,4]] gives [1,2,4,3]. An empty matrix gives []. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 259 tokens in 46.3s, finish: stop
- verifier: pass

```python
def spiral_order(matrix):
    if not matrix or not matrix[0]:
        return []
    
    result = []
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # Traverse from left to right along the top row
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
        
        # Traverse from top to bottom along the right column
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        
        # Traverse from right to left along the bottom row
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
        bottom -= 1
        
        # Traverse from bottom to top along the left column
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
        left += 1
    
    return result
```
