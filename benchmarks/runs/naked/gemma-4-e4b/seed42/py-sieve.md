# gemma-4-e4b / py-sieve / seed 42 / naked

## Prompt

Write a Python function `count_primes(n)` returning how many prime numbers are <= n (n may be 0 or 1). It is tested with n = 3,000,000, so trial division is too slow. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 309 tokens in 47.4s, finish: stop

```python
def count_primes(n):
    """
    Counts the number of prime numbers less than or equal to n using the Sieve of Eratosthenes.
    """
    if n < 2:
        return 0

    # Initialize a boolean array "is_prime" of size n+1, setting all entries to True.
    # is_prime[i] will be False if i is composite, True if i is prime.
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

    p = 2
    while (p * p <= n):
        # If is_prime[p] is not changed, then it is a prime
        if is_prime[p]:
            # Update all multiples of p starting from p*p
            # Multiples smaller than p*p would have already been marked by smaller primes
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    # Count the number of True values in the is_prime array
    count = 0
    for i in range(2, n + 1):
        if is_prime[i]:
            count += 1
    return count
```
