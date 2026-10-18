# qwen2.5-coder-3b / py-sieve / seed 42 / harness

## Prompt

Write a Python function `count_primes(n)` returning how many prime numbers are <= n (n may be 0 or 1). It is tested with n = 3,000,000, so trial division is too slow. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: AssertionError)

- 104 tokens in 10.8s, finish: stop
- verifier: pass

```python
def count_primes(n):
    if n <= 2:
        return 0
    count = 1
    for i in range(3, n + 1, 2):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return count
```
