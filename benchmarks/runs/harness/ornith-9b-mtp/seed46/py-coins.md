# ornith-9b-mtp / py-coins / seed 46 / harness

## Prompt

Write a Python function `min_coins(coins, amount)` returning the minimum number of coins (unlimited supply of each denomination) needed to make `amount`, or -1 if impossible. min_coins(coins, 0) is 0. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 132 tokens in 26.2s, finish: stop
- verifier: pass

```python
def min_coins(coins, amount):
    if amount == 0:
        return 0
    
    INF = float('inf')
    dp = [INF] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for c in coins:
            if c <= i and dp[i - c] != INF:
                dp[i] = min(dp[i], dp[i - c] + 1)
    
    return dp[amount] if dp[amount] != INF else -1
```
