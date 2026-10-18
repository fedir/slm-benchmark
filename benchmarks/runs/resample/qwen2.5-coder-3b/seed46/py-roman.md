# qwen2.5-coder-3b / py-roman / seed 46 / resample (no feedback)

## Prompt

Write a Python function `to_roman(n)` converting an integer 1..3999 to its Roman numeral (standard subtractive form, e.g. 4 is IV, 1994 is MCMXCIV). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 153 tokens in 14.8s, finish: stop
- verifier: pass

```python
def to_roman(n):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_numeral = ""
    for i in range(len(val)):
        while n >= val[i]:
            roman_numeral += syms[i]
            n -= val[i]
    return roman_numeral
```
