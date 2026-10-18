# nemotron-3-nano-4b / py-coins / seed 42 / harness

## Prompt

Write a Python function `min_coins(coins, amount)` returning the minimum number of coins (unlimited supply of each denomination) needed to make `amount`, or -1 if impossible. min_coins(coins, 0) is 0. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: ValueError: min() iterable argument is empty)

- 117 tokens in 20.3s, finish: stop
- verifier: FAIL: min_coins([2,5],7) raised ValueError: min() iterable argument is empty; min_coins([3],7) raised ValueError: min() iterable argument is empty

```python
def min_coins(coins, amount):
    if amount == 0:
        return 0
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        dp[i] = min(dp[i - c] + 1 for c in coins if i >= c and dp[i - c] != float('inf'))
    return dp[amount] if dp[amount] != float('inf') else -1
```

## Attempt 2: PASS (hidden: tests passed)

- 132 tokens in 30.9s, finish: stop
- verifier: pass

```python
def min_coins(coins, amount):
    if amount == 0:
        return 0
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        available = [dp[i - c] + 1 for c in coins if i >= c and dp[i - c] != float('inf')]
        dp[i] = min(available) if available else float('inf')
    return dp[amount] if dp[amount] != float('inf') else -1
```
