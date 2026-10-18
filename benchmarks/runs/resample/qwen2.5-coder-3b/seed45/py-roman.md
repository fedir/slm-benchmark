# qwen2.5-coder-3b / py-roman / seed 45 / resample (no feedback)

## Prompt

Write a Python function `to_roman(n)` converting an integer 1..3999 to its Roman numeral (standard subtractive form, e.g. 4 is IV, 1994 is MCMXCIV). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 203 tokens in 19.1s, finish: stop
- verifier: pass

```python
def to_roman(n):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_numeral = ''
    i = 0
    while n > 0:
        for _ in range(n // val[i]):
            roman_numeral += syms[i]
            n -= val[i]
        i += 1
    return roman_numeral
```

This function converts an integer to its Roman numeral representation, handling values up to 3999.
