# qwen2.5-coder-3b / py-parens / seed 43 / harness

## Prompt

Write a Python function `is_balanced(s)` returning True if the brackets `()`, `[]` and `{}` in the string are balanced and correctly nested, else False. Other characters are ignored; the empty string is balanced. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 89 tokens in 9.9s, finish: stop
- verifier: pass

```python
def is_balanced(s):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if stack and stack[-1] == brackets[char]:
                stack.pop()
            else:
                return False
    
    return len(stack) == 0
```
