# ornith-9b-mtp / py-roman / seed 45 / harness

## Prompt

Write a Python function `to_roman(n)` converting an integer 1..3999 to its Roman numeral (standard subtractive form, e.g. 4 is IV, 1994 is MCMXCIV). Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: AssertionError)

- 168 tokens in 32.7s, finish: stop
- verifier: FAIL: to_roman(3) returned '', expected 'III'; to_roman(49) returned '', expected 'XLIX'; to_roman(900) returned '', expected 'CM'

```python
def to_roman(n):
    table = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
    ]
    result = []
    for value, numeral in table:
        while n >= value:
            n -= value
            result.append(numeral)
        if not result:
            break
    return "".join(result)
```

## Attempt 2: PASS (hidden: tests passed)

- 159 tokens in 36.5s, finish: stop
- verifier: pass

```python
def to_roman(n):
    table = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
    ]
    result = []
    for value, numeral in table:
        while n >= value:
            n -= value
            result.append(numeral)
    return "".join(result)
```
