# gemma-4-e4b-p-oneline-rule / py-sieve / seed 43 / naked

## Prompt

Write a Python function `count_primes(n)` returning how many prime numbers are <= n (n may be 0 or 1). It is tested with n = 3,000,000, so trial division is too slow. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 156 tokens in 26.7s, finish: stop

```python
def count_primes(n):
    if n < 2:
        return 0
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    count = 0
    for i in range(2, n + 1):
        if is_prime[i]:
            count += 1
    return count
```
