# gemma-4-e4b / py-roman / seed 42 / naked

## Prompt

Write a Python function `to_roman(n)` converting an integer 1..3999 to its Roman numeral (standard subtractive form, e.g. 4 is IV, 1994 is MCMXCIV). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 395 tokens in 59.1s, finish: stop

```python
def to_roman(n):
    """
    Converts an integer (1..3999) to its Roman numeral representation.
    """
    mapping = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
        50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }
    
    roman = ""
    
    # Get the keys in descending order to ensure largest values are processed first
    values = sorted(mapping.keys(), reverse=True)
    
    for value in values:
        while n >= value:
            roman += mapping[value]
            n -= value
            
    return roman

if __name__ == '__main__':
    # Test cases
    print(f"3: {to_roman(3)}")     # III
    print(f"4: {to_roman(4)}")     # IV
    print(f"9: {to_roman(9)}")     # IX
    print(f"14: {to_roman(14)}")   # XIV
    print(f"58: {to_roman(58)}")   # LVIII
    print(f"1994: {to_roman(1994)}") # MCMXCIV
    print(f"3999: {to_roman(3999)}") # MMMCMXCIX
    print(f"1: {to_roman(1)}")     # I
```
