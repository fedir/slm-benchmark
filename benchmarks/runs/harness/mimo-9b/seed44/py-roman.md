# mimo-9b / py-roman / seed 44 / harness

## Prompt

Write a Python function `to_roman(n)` converting an integer 1..3999 to its Roman numeral (standard subtractive form, e.g. 4 is IV, 1994 is MCMXCIV). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 210 tokens in 72.9s, finish: stop
- verifier: pass

```python
def to_roman(n):
    """Convert an integer (1..3999) to its standard Roman numeral."""
    if not 1 <= n <= 3999:
        raise ValueError("Input must be between 1 and 3999")

    values = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
    ]

    roman, remaining = "", n
    for value, symbol in values:
        while remaining >= value:
            roman += symbol
            remaining -= value
    return roman
```
