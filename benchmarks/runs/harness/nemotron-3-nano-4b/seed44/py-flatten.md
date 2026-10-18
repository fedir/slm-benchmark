# nemotron-3-nano-4b / py-flatten / seed 44 / harness

## Prompt

Write a Python function `flatten(x)` that flattens an arbitrarily nested list of integers into a flat list, keeping the order, e.g. [1,[2,[3]],4] becomes [1,2,3,4]. Nesting can be up to 5000 levels deep. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: RecursionError: maximum recursion depth exceeded)

- 42 tokens in 8.5s, finish: stop
- verifier: FAIL: the performance example raised RecursionError: maximum recursion depth exceeded

```python
def flatten(x):
    if isinstance(x, list):
        result = []
        for item in x:
            result.extend(flatten(item))
        return result
    return [x]
```

## Attempt 2: PASS (hidden: tests passed)

- 55 tokens in 11.7s, finish: stop
- verifier: pass

```python
def flatten(x):
    result = []
    stack = [x]
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            stack.extend(reversed(current))
        else:
            result.append(current)
    return result
```
