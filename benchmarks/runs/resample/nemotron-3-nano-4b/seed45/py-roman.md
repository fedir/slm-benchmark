# nemotron-3-nano-4b / py-roman / seed 45 / resample (no feedback)

## Prompt

Write a Python function `to_roman(n)` converting an integer 1..3999 to its Roman numeral (standard subtractive form, e.g. 4 is IV, 1994 is MCMXCIV). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 192 tokens in 29.5s, finish: stop
- verifier: pass

```python
def to_roman(n):
    if not 1 <= n <= 3999:
        raise ValueError("Roman numerals only represent integers from 1 to 3999.")
    val_sym = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]
    res = ""
    for value, symbol in val_sym:
        while n >= value:
            n -= value
            res += symbol
    return res
```
