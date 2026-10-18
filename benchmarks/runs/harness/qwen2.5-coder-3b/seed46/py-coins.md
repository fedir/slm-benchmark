# qwen2.5-coder-3b / py-coins / seed 46 / harness

## Prompt

Write a Python function `min_coins(coins, amount)` returning the minimum number of coins (unlimited supply of each denomination) needed to make `amount`, or -1 if impossible. min_coins(coins, 0) is 0. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 117 tokens in 11.7s, finish: stop
- verifier: pass

```python
def min_coins(coins, amount):
    if amount == 0:
        return 0
    if not coins:
        return -1

    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for j in range(coin, amount + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1
```
