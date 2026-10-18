# gemma-4-e4b-p-code-only / py-roman / seed 43 / naked

## Prompt

Write a Python function `to_roman(n)` converting an integer 1..3999 to its Roman numeral (standard subtractive form, e.g. 4 is IV, 1994 is MCMXCIV). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 169 tokens in 27.6s, finish: stop

```python
def to_roman(n):
    mapping = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }
    result = ""
    sorted_values = sorted(mapping.keys(), reverse=True)
    for value in sorted_values:
        while n >= value:
            result += mapping[value]
            n -= value
    return result
```
