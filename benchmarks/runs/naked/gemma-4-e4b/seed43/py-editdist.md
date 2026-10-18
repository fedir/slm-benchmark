# gemma-4-e4b / py-editdist / seed 43 / naked

## Prompt

Write a Python function `edit_distance(a, b)` returning the Levenshtein edit distance between two strings (insert, delete, replace, each cost 1). It is tested on strings of 1500 characters. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 402 tokens in 62.6s, finish: stop

```python
def edit_distance(a, b):
    """
    Calculates the Levenshtein edit distance between two strings.

    Args:
        a: The first string.
        b: The second string.

    Returns:
        The Levenshtein edit distance (integer).
    """
    m = len(a)
    n = len(b)

    # Create a matrix to store the distances
    # dp[i][j] will be the edit distance between a[:i] and b[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row and column
    # Distance between any string and an empty string
    for i in range(m + 1):
        dp[i][0] = i  # i deletions to transform a[:i] to ""
    for j in range(n + 1):
        dp[0][j] = j  # j insertions to transform "" to b[:j]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Cost of substitution: 0 if characters match, 1 otherwise
            cost = 0 if a[i - 1] == b[j - 1] else 1

            dp[i][j] = min(
                dp[i - 1][j] + 1,        # Deletion (from a)
                dp[i][j - 1] + 1,        # Insertion (to a, or deletion from b)
                dp[i - 1][j - 1] + cost  # Substitution or Match
            )

    return dp[m][n]
```
