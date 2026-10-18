# gemma-4-e4b-mtp / py-roman / seed 42 / naked

## Prompt

Write a Python function `to_roman(n)` converting an integer 1..3999 to its Roman numeral (standard subtractive form, e.g. 4 is IV, 1994 is MCMXCIV). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 234 tokens in 26.9s, finish: stop

```python
def to_roman(n):
    """
    Converts an integer (1..3999) to its Roman numeral representation.
    """
    if not 1 <= n <= 3999:
        raise ValueError("Input must be between 1 and 3999")

    roman_map = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
        90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
        5: 'V', 4: 'IV', 1: 'I'
    }

    result = ""
    # Iterate through the keys in descending order to ensure correct greedy subtraction
    for value, symbol in roman_map.items():
        while n >= value:
            result += symbol
            n -= value
            
    return result
```
