# gemma-4-e4b / py-coins / seed 42 / naked

## Prompt

Write a Python function `min_coins(coins, amount)` returning the minimum number of coins (unlimited supply of each denomination) needed to make `amount`, or -1 if impossible. min_coins(coins, 0) is 0. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 330 tokens in 50.4s, finish: stop

```python
def min_coins(coins, amount):
    """
    Calculates the minimum number of coins needed to make a given amount.

    Args:
        coins: A list of available coin denominations.
        amount: The target amount.

    Returns:
        The minimum number of coins, or -1 if impossible.
    """
    if amount == 0:
        return 0

    # Initialize dp array. dp[i] will store the minimum coins needed for amount i.
    # Initialize with amount + 1 (a value larger than any possible solution)
    dp = [amount + 1] * (amount + 1)

    # Base case: 0 coins needed for amount 0
    dp[0] = 0

    # Iterate through all amounts from 1 up to the target amount
    for i in range(1, amount + 1):
        # Try every coin denomination
        for coin in coins:
            if i - coin >= 0:
                # Update dp[i] if using this coin leads to a smaller count
                # The new count is 1 (for the current coin) + minimum coins for the remaining amount (i - coin)
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[amount] is still greater than amount, it means it was impossible to form the amount
    return dp[amount] if dp[amount] <= amount else -1
```
