# gemma-4-e4b / py-roman / seed 43 / naked

## Prompt

Write a Python function `to_roman(n)` converting an integer 1..3999 to its Roman numeral (standard subtractive form, e.g. 4 is IV, 1994 is MCMXCIV). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 389 tokens in 60.6s, finish: stop

```python
def to_roman(n):
    """
    Converts an integer (1..3999) to its Roman numeral representation.
    Uses standard subtractive notation (e.g., 4 is IV, 1994 is MCMXCIV).
    """
    mapping = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }
    
    roman_numeral = ""
    
    # Iterate through the values in descending order
    for value, symbol in mapping.items():
        while n >= value:
            roman_numeral += symbol
            n -= value
            
    return roman_numeral

if __name__ == '__main__':
    # Test cases
    print(f"3: {to_roman(3)}")       # III
    print(f"4: {to_roman(4)}")       # IV
    print(f"9: {to_roman(9)}")       # IX
    print(f"58: {to_roman(58)}")     # LVIII
    print(f"1994: {to_roman(1994)}") # MCMXCIV
    print(f"3999: {to_roman(3999)}") # MMMCMXCIX
    print(f"1: {to_roman(1)}")       # I
```
