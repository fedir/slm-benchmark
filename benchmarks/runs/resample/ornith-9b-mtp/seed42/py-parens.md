# ornith-9b-mtp / py-parens / seed 42 / resample (no feedback)

## Prompt

Write a Python function `is_balanced(s)` returning True if the brackets `()`, `[]` and `{}` in the string are balanced and correctly nested, else False. Other characters are ignored; the empty string is balanced. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 107 tokens in 23.2s, finish: stop
- verifier: pass

```python
def is_balanced(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    openers = set(pairs.values())

    for char in s:
        if char in openers:
            stack.append(char)
        elif char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
        # other characters are ignored

    return not stack
```
