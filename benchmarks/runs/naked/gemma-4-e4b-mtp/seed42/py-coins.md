# gemma-4-e4b-mtp / py-coins / seed 42 / naked

## Prompt

Write a Python function `min_coins(coins, amount)` returning the minimum number of coins (unlimited supply of each denomination) needed to make `amount`, or -1 if impossible. min_coins(coins, 0) is 0. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 286 tokens in 32.5s, finish: stop

```python
def min_coins(coins, amount):
    """
    Calculates the minimum number of coins needed to make a given amount.

    Args:
        coins (list): A list of coin denominations.
        amount (int): The target amount.

    Returns:
        int: The minimum number of coins, or -1 if impossible.
    """
    if amount == 0:
        return 0

    # dp[i] will store the minimum number of coins needed to make amount i
    # Initialize with amount + 1, representing infinity (since the max possible coins is amount if all coins are 1)
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                # Update dp[i] using the minimum of its current value and 1 + minimum coins for the remaining amount (i - coin)
                dp[i] = min(dp[i], 1 + dp[i - coin])

    # If dp[amount] is still amount + 1, it means the amount is unreachable
    return dp[amount] if dp[amount] <= amount else -1
```
