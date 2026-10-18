# mimo-9b / py-roman / seed 42 / harness

## Prompt

Write a Python function `to_roman(n)` converting an integer 1..3999 to its Roman numeral (standard subtractive form, e.g. 4 is IV, 1994 is MCMXCIV). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 302 tokens in 79.5s, finish: stop
- verifier: pass

```python
def to_roman(n):
    """Convert an integer (1..3999) to a Roman numeral using standard
    subtractive notation (e.g. 4 -> IV, 9 -> IX, 1994 -> MCMXCIV)."""
    if not 1 <= n <= 3999:
        raise ValueError("n must be in the range 1..3999")

    # (value, roman symbol) pairs in descending order, including the
    # subtractive combinations (4/9/40/90/400/900).
    roman_map = [
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
        (1, "I"),
    ]

    roman = ""
    for value, symbol in roman_map:
        while n >= value:
            roman += symbol
            n -= value
    return roman
```
