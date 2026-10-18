# nemotron-3-nano-4b / py-roman / seed 42 / harness

## Prompt

Write a Python function `to_roman(n)` converting an integer 1..3999 to its Roman numeral (standard subtractive form, e.g. 4 is IV, 1994 is MCMXCIV). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 206 tokens in 31.3s, finish: stop
- verifier: pass

```python
def to_roman(n):
    if not (1 <= n <= 3999):
        raise ValueError("Input must be between 1 and 3999")
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4, 1
    ]
    sym = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV", "I"
    ]
    roman = ""
    i = 0
    while n > 0:
        count = n // val[i]
        roman += sym[i] * count
        n %= val[i]
        i += 1
    return roman
```
