# qwen2.5-coder-3b / py-coins

- category: python
- result: **PASS** (tests passed)
- tokens: 107 in 11s (10.2 t/s), finish: stop

## Prompt

Write a Python function `min_coins(coins, amount)` returning the minimum number of coins (unlimited supply of each denomination) needed to make `amount`, or -1 if impossible. min_coins(coins, 0) is 0. Reply with ONLY the code in one code block.

## Answer

```python
def min_coins(coins, amount):
    if amount == 0:
        return 0
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1
```
