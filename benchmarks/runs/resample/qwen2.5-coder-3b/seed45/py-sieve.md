# qwen2.5-coder-3b / py-sieve / seed 45 / resample (no feedback)

## Prompt

Write a Python function `count_primes(n)` returning how many prime numbers are <= n (n may be 0 or 1). It is tested with n = 3,000,000, so trial division is too slow. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 198 tokens in 18.8s, finish: stop
- verifier: pass

```python
from math import sqrt

def count_primes(n):
    if n < 2:
        return 0
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(sqrt(n)) + 1):
        if primes[i]:
            for j in range(i*i, n + 1, i):
                primes[j] = False
    return sum(primes)

# Test the function
print(count_primes(3000000))
```
This function uses the Sieve of Eratosthenes algorithm for efficient prime counting up to `n`. It initializes a boolean array `primes` of size `n + 1`, marking all numbers as prime initially. It then iterates over each number starting from 2, marking its multiples as non-prime. Finally, it returns the count of primes found.
