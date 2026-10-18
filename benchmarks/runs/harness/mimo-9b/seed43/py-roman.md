# mimo-9b / py-roman / seed 43 / harness

## Prompt

Write a Python function `to_roman(n)` converting an integer 1..3999 to its Roman numeral (standard subtractive form, e.g. 4 is IV, 1994 is MCMXCIV). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed (no code fence))

- 218 tokens in 59.5s, finish: stop
- verifier: pass

def to_roman(n):
    """Convert an integer (1..3999) to its standard Roman numeral."""
    if not 1 <= n <= 3999:
        raise ValueError(f"to_roman() only accepts integers in range 1..3999, got {n}")

    roman_values = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
    ]

    result = []
    for value, numeral in roman_values:
        while n >= value:
            result.append(numeral)
            n -= value
    return "".join(result)
