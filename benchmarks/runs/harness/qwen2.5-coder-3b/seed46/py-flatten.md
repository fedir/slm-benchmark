# qwen2.5-coder-3b / py-flatten / seed 46 / harness

## Prompt

Write a Python function `flatten(x)` that flattens an arbitrarily nested list of integers into a flat list, keeping the order, e.g. [1,[2,[3]],4] becomes [1,2,3,4]. Nesting can be up to 5000 levels deep. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: RecursionError: maximum recursion depth exceeded)

- 45 tokens in 5.5s, finish: stop
- verifier: FAIL: the performance example raised RecursionError: maximum recursion depth exceeded

```python
def flatten(x):
    result = []
    for item in x:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
```

## Attempt 2: FAIL (hidden: AssertionError)

- 53 tokens in 6.8s, finish: stop
- verifier: FAIL: flatten([[1],[2,[3]]]) returned [3, 2, 1], expected [1,2,3]

```python
def flatten(x):
    result = []
    stack = [x]
    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(item)
        else:
            result.append(item)
    return result
```

## Attempt 3: PASS (hidden: tests passed)

- 65 tokens in 9.2s, finish: stop
- verifier: pass

```python
def flatten(x):
    result = []
    stack = [x]
    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(item[::-1])  # Extend from the end to maintain order
        else:
            result.append(item)
    return result
```
