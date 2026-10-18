# gemma-4-e4b-p-code-only / py-roman / seed 42 / naked

## Prompt

Write a Python function `to_roman(n)` converting an integer 1..3999 to its Roman numeral (standard subtractive form, e.g. 4 is IV, 1994 is MCMXCIV). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 169 tokens in 27.6s, finish: stop

```python
def to_roman(n):
    values = [
        1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
    ]
    symbols = [
        "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"
    ]
    result = ""
    for i in range(len(values)):
        while n >= values[i]:
            result += symbols[i]
            n -= values[i]
    return result
```
