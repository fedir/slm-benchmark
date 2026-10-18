# nemotron-3-nano-4b / py-flatten / seed 42 / harness

## Prompt

Write a Python function `flatten(x)` that flattens an arbitrarily nested list of integers into a flat list, keeping the order, e.g. [1,[2,[3]],4] becomes [1,2,3,4]. Nesting can be up to 5000 levels deep. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: RecursionError: maximum recursion depth exceeded)

- 45 tokens in 8.9s, finish: stop
- verifier: FAIL: the performance example raised RecursionError: maximum recursion depth exceeded

```python
def flatten(x):
    result = []
    if isinstance(x, list):
        for item in x:
            result.extend(flatten(item))
    else:
        result.append(x)
    return result
```

## Attempt 2: PASS (hidden: tests passed)

- 55 tokens in 12.5s, finish: stop
- verifier: pass

```python
def flatten(x):
    result = []
    stack = [x]
    while stack:
        node = stack.pop()
        if isinstance(node, list):
            stack.extend(reversed(node))
        else:
            result.append(node)
    return result
```
