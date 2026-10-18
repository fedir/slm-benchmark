# gemma-4-e4b-concise / py-flatten / seed 42 / harness

## Prompt

Write a Python function `flatten(x)` that flattens an arbitrarily nested list of integers into a flat list, keeping the order, e.g. [1,[2,[3]],4] becomes [1,2,3,4]. Nesting can be up to 5000 levels deep. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: RecursionError: maximum recursion depth exceeded)

- 56 tokens in 12.3s, finish: stop
- verifier: FAIL: the performance example raised RecursionError: maximum recursion depth exceeded

```python
def flatten(x):
    if isinstance(x, list):
        result = []
        for item in x:
            result.extend(flatten(item))
        return result
    else:
        return [x]
```

## Attempt 2: PASS (hidden: tests passed)

- 71 tokens in 17.2s, finish: stop
- verifier: pass

```python
def flatten(x):
    stack = [x]
    result = []
    while stack:
        element = stack.pop()
        if isinstance(element, list):
            stack.extend(reversed(element))
        else:
            result.append(element)
    return result
```
