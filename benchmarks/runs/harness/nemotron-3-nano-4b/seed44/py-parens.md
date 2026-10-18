# nemotron-3-nano-4b / py-parens / seed 44 / harness

## Prompt

Write a Python function `is_balanced(s)` returning True if the brackets `()`, `[]` and `{}` in the string are balanced and correctly nested, else False. Other characters are ignored; the empty string is balanced. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 82 tokens in 13.4s, finish: stop
- verifier: pass

```python
def is_balanced(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack.pop() != mapping[char]:
                return False
    return not stack
```
