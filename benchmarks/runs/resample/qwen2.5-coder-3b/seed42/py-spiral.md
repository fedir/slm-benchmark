# qwen2.5-coder-3b / py-spiral / seed 42 / resample (no feedback)

## Prompt

Write a Python function `spiral_order(matrix)` returning the elements of a rectangular matrix (list of lists) in clockwise spiral order starting at the top-left, e.g. [[1,2],[3,4]] gives [1,2,4,3]. An empty matrix gives []. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 252 tokens in 23.9s, finish: stop
- verifier: pass

```python
def spiral_order(matrix):
    if not matrix or not matrix[0]:
        return []
    
    result = []
    row_start, row_end = 0, len(matrix) - 1
    col_start, col_end = 0, len(matrix[0]) - 1
    
    while row_start <= row_end and col_start <= col_end:
        # Traverse the top row
        for col in range(col_start, col_end + 1):
            result.append(matrix[row_start][col])
        row_start += 1
        
        # Traverse the right column
        for row in range(row_start, row_end + 1):
            result.append(matrix[row][col_end])
        col_end -= 1
        
        if row_start <= row_end:
            # Traverse the bottom row
            for col in range(col_end, col_start - 1, -1):
                result.append(matrix[row_end][col])
            row_end -= 1
        
        if col_start <= col_end:
            # Traverse the left column
            for row in range(row_end, row_start - 1, -1):
                result.append(matrix[row][col_start])
            col_start += 1
    
    return result
```
