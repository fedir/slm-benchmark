# mimo-9b / py-coins

- category: python
- result: **PASS** (tests passed (no code fence))
- tokens: 113 in 35s (3.2 t/s), finish: stop

## Prompt

Write a Python function `min_coins(coins, amount)` returning the minimum number of coins (unlimited supply of each denomination) needed to make `amount`, or -1 if impossible. min_coins(coins, 0) is 0. Reply with ONLY the code in one code block.

## Answer

def min_coins(coins, amount):
    if amount == 0:
        return 0

    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] <= amount else -1
