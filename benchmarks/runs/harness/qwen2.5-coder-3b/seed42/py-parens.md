# qwen2.5-coder-3b / py-parens / seed 42 / harness

## Prompt

Write a Python function `is_balanced(s)` returning True if the brackets `()`, `[]` and `{}` in the string are balanced and correctly nested, else False. Other characters are ignored; the empty string is balanced. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 88 tokens in 9.4s, finish: stop
- verifier: pass

```python
def is_balanced(s):
    stack = []
    match = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in match.values():
            stack.append(char)
        elif char in match.keys():
            if not stack or stack.pop() != match[char]:
                return False
        else:
            continue
    
    return len(stack) == 0
```
