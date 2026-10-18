# qwen2.5-coder-3b / py-editdist / seed 42 / harness

## Prompt

Write a Python function `edit_distance(a, b)` returning the Levenshtein edit distance between two strings (insert, delete, replace, each cost 1). It is tested on strings of 1500 characters. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 284 tokens in 26.9s, finish: stop
- verifier: pass

```python
def edit_distance(a, b):
    # Create a table to store distances
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    
    # Initialize the table
    for i in range(len(a) + 1):
        dp[i][0] = i
    for j in range(len(b) + 1):
        dp[0][j] = j
    
    # Fill the table
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                cost = 0
            else:
                cost = 1
            dp[i][j] = min(dp[i - 1][j] + 1,  # Deletion
                          dp[i][j - 1] + 1,  # Insertion
                          dp[i - 1][j - 1] + cost)  # Substitution
    
    # The distance is in the bottom-right cell
    return dp[len(a)][len(b)]
```

This function implements the dynamic programming approach to calculate the Levenshtein edit distance between two strings, where each operation (insert, delete, replace) has a cost of 1.
