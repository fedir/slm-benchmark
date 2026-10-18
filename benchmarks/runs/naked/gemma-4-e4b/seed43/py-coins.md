# gemma-4-e4b / py-coins / seed 43 / naked

## Prompt

Write a Python function `min_coins(coins, amount)` returning the minimum number of coins (unlimited supply of each denomination) needed to make `amount`, or -1 if impossible. min_coins(coins, 0) is 0. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 265 tokens in 42.9s, finish: stop

```python
def min_coins(coins, amount):
    """
    Calculates the minimum number of coins needed to make the amount.

    Args:
        coins (list): A list of coin denominations.
        amount (int): The target amount.

    Returns:
        int: The minimum number of coins, or -1 if impossible.
    """
    if amount == 0:
        return 0

    # dp[i] will store the minimum number of coins needed to make amount i
    # Initialize with amount + 1, which represents infinity for this problem
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                # Update dp[i] if using the current coin leads to a smaller count
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[amount] is still greater than amount, it means it's impossible
    return dp[amount] if dp[amount] <= amount else -1
```
