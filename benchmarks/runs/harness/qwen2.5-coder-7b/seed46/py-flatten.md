# qwen2.5-coder-7b / py-flatten / seed 46 / harness

## Prompt

Write a Python function `flatten(x)` that flattens an arbitrarily nested list of integers into a flat list, keeping the order, e.g. [1,[2,[3]],4] becomes [1,2,3,4]. Nesting can be up to 5000 levels deep. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: RecursionError: maximum recursion depth exceeded)

- 45 tokens in 12.2s, finish: stop
- verifier: FAIL: the performance example raised RecursionError: maximum recursion depth exceeded

```python
def flatten(x):
    result = []
    for i in x:
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result
```

## Attempt 2: FAIL (hidden: AssertionError)

- 58 tokens in 16.1s, finish: stop
- verifier: FAIL: flatten([[1],[2,[3]]]) returned [3, 2, 1], expected [1,2,3]

```python
def flatten(x):
    result = []
    stack = x[::-1]
    while stack:
        top = stack.pop()
        if isinstance(top, list):
            stack.extend(top[::-1])
        else:
            result.append(top)
    return result[::-1]
```

## Attempt 3: FAIL (hidden: AssertionError)

- 58 tokens in 19.0s, finish: stop
- verifier: FAIL: flatten([[1],[2,[3]]]) returned [3, 2, 1], expected [1,2,3]

```python
def flatten(x):
    result = []
    stack = x[::-1]
    while stack:
        top = stack.pop()
        if isinstance(top, list):
            stack.extend(top[::-1])
        else:
            result.append(top)
    return result[::-1]
```
