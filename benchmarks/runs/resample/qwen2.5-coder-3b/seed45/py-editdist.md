# qwen2.5-coder-3b / py-editdist / seed 45 / resample (no feedback)

## Prompt

Write a Python function `edit_distance(a, b)` returning the Levenshtein edit distance between two strings (insert, delete, replace, each cost 1). It is tested on strings of 1500 characters. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 226 tokens in 21.2s, finish: stop
- verifier: pass

```python
def edit_distance(a, b):
    len_a = len(a)
    len_b = len(b)
    
    # Initialize the matrix for dynamic programming
    dp = [[0] * (len_b + 1) for _ in range(len_a + 1)]
    
    # Fill the matrix
    for i in range(len_a + 1):
        for j in range(len_b + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            else:
                if a[i - 1] == b[j - 1]:
                    cost = 0
                else:
                    cost = 1
                dp[i][j] = min(dp[i - 1][j] + 1,  # Deletion
                                dp[i][j - 1] + 1,  # Insertion
                                dp[i - 1][j - 1] + cost)  # Substitution
    
    return dp[len_a][len_b]
```
