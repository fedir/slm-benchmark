# qwen2.5-coder-7b / py-parens / seed 44 / resample (no feedback)

## Prompt

Write a Python function `is_balanced(s)` returning True if the brackets `()`, `[]` and `{}` in the string are balanced and correctly nested, else False. Other characters are ignored; the empty string is balanced. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 77 tokens in 18.3s, finish: stop
- verifier: pass

```python
def is_balanced(s):
    stack = []
    mapping = {")": "(", "]": "[", "}": "{"}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if stack == [] or mapping[char] != stack.pop():
                return False
    return stack == []
```
