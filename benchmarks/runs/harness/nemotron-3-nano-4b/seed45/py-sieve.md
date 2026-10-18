# nemotron-3-nano-4b / py-sieve / seed 45 / harness

## Prompt

Write a Python function `count_primes(n)` returning how many prime numbers are <= n (n may be 0 or 1). It is tested with n = 3,000,000, so trial division is too slow. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 107 tokens in 17.5s, finish: stop
- verifier: pass

```python
def count_primes(n):
    if n < 2:
        return 0
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i : n+1 : i] = [False] * len(sieve[i*i : n+1 : i])
    return sum(sieve)
```
