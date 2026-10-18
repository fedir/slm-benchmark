# gemma-4-e4b / py-parens / seed 42 / naked

## Prompt

Write a Python function `is_balanced(s)` returning True if the brackets `()`, `[]` and `{}` in the string are balanced and correctly nested, else False. Other characters are ignored; the empty string is balanced. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 161 tokens in 25.1s, finish: stop

```python
def is_balanced(s):
    """
    Checks if the brackets (), [], and {} in the string are balanced and correctly nested.
    Other characters are ignored; the empty string is balanced.
    """
    stack = []
    mapping = {")": "(", "]": "[", "}": "{"}
    opening_brackets = set("([{")

    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in mapping:
            if not stack:
                return False
            top_element = stack.pop()
            if top_element != mapping[char]:
                return False
        # Ignore other characters

    return not stack
```
