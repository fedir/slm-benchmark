# ornith-9b-mtp / py-spiral / seed 43 / harness

## Prompt

Write a Python function `spiral_order(matrix)` returning the elements of a rectangular matrix (list of lists) in clockwise spiral order starting at the top-left, e.g. [[1,2],[3,4]] gives [1,2,4,3]. An empty matrix gives []. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: AssertionError)

- 207 tokens in 38.0s, finish: stop
- verifier: FAIL: spiral_order([[1,2],[3,4],[5,6]]) returned [1, 2, 4, 6, 3], expected [1,2,4,6,5,3]; spiral_order([[1,2,3],[4,5,6]]) returned [1, 2, 3, 6, 5], expected [1,2,3,6,5,4]

```python
def spiral_order(matrix):
    if not matrix:
        return []
    
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
        
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        
        if top <= bottom:
            for col in range(right, top - 1, -1):
                result.append(matrix[bottom][col])
        bottom -= 1
        
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
        left += 1
    
    return result
```

## Attempt 2: FAIL (hidden: AssertionError)

- 212 tokens in 48.2s, finish: stop
- verifier: FAIL: spiral_order([[1,2],[3,4],[5,6]]) returned [1, 2, 4, 6, 3], expected [1,2,4,6,5,3]; spiral_order([[1,2,3],[4,5,6]]) returned [1, 2, 3, 6, 5], expected [1,2,3,6,5,4]

```python
def spiral_order(matrix):
    if not matrix or not matrix[0]:
        return []
    
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
        
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        
        if top <= bottom:
            for col in range(right, top - 1, -1):
                result.append(matrix[bottom][col])
        bottom -= 1
        
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
        left += 1
    
    return result
```

## Attempt 3: FAIL (hidden: AssertionError)

- 207 tokens in 57.7s, finish: stop
- verifier: FAIL: spiral_order([[1,2],[3,4],[5,6]]) returned [1, 2, 4, 6, 3], expected [1,2,4,6,5,3]; spiral_order([[1,2,3],[4,5,6]]) returned [1, 2, 3, 6, 5], expected [1,2,3,6,5,4]

```python
def spiral_order(matrix):
    if not matrix:
        return []
    
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
        
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        
        if top <= bottom:
            for col in range(right, top - 1, -1):
                result.append(matrix[bottom][col])
        bottom -= 1
        
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
        left += 1
    
    return result
```
