# qwen2.5-coder-3b / py-sieve / seed 46 / harness

## Prompt

Write a Python function `count_primes(n)` returning how many prime numbers are <= n (n may be 0 or 1). It is tested with n = 3,000,000, so trial division is too slow. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 103 tokens in 10.5s, finish: stop
- verifier: pass

```python
def count_primes(n):
    if n < 2:
        return 0
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for start in range(2, int(n**0.5) + 1):
        if primes[start]:
            for multiple in range(start * start, n + 1, start):
                primes[multiple] = False
    return sum(primes)
```
