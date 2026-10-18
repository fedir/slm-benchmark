# qwen2.5-coder-3b / py-coins / seed 43 / resample (no feedback)

## Prompt

Write a Python function `min_coins(coins, amount)` returning the minimum number of coins (unlimited supply of each denomination) needed to make `amount`, or -1 if impossible. min_coins(coins, 0) is 0. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 165 tokens in 15.7s, finish: stop
- verifier: pass

```python
def min_coins(coins, amount):
    # Initialize the dp array with a large number for each amount
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins needed to make amount 0
    
    # Iterate over each coin denomination
    for coin in coins:
        # Update the dp array for each possible amount
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If dp[amount] is still infinity, it means it's not possible to make the amount
    return dp[amount] if dp[amount] != float('inf') else -1
```
