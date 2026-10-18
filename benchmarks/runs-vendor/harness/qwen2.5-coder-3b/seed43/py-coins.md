# qwen2.5-coder-3b / py-coins / seed 43 / harness

## Prompt

Write a Python function `min_coins(coins, amount)` returning the minimum number of coins (unlimited supply of each denomination) needed to make `amount`, or -1 if impossible. min_coins(coins, 0) is 0. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 175 tokens in 16.9s, finish: stop
- verifier: pass

```python
def min_coins(coins, amount):
    # Initialize a list to store the minimum coins needed for each amount up to amount
    dp = [float('inf')] * (amount + 1)
    
    # Base case: 0 coins are needed to make amount 0
    dp[0] = 0
    
    # Iterate through each coin value
    for coin in coins:
        # Update the dp list for each possible amount from coin to amount
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If dp[amount] is still infinity, it means it's impossible to make that amount
    return dp[amount] if dp[amount] != float('inf') else -1
```
