# ornith-9b-mtp / py-sieve / seed 45 / resample (no feedback)

## Prompt

Write a Python function `count_primes(n)` returning how many prime numbers are <= n (n may be 0 or 1). It is tested with n = 3,000,000, so trial division is too slow. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 127 tokens in 25.6s, finish: stop
- verifier: pass

```python
def count_primes(n):
    if n < 2:
        return 0
    is_prime = bytearray([1]) * (n + 1)
    is_prime[0] = is_prime[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            is_prime[i * i::i] = bytearray(len(is_prime[i * i::i]))
    return sum(is_prime)

print(count_primes(3000000))
```
