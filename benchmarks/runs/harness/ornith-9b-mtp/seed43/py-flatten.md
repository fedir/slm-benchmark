# ornith-9b-mtp / py-flatten / seed 43 / harness

## Prompt

Write a Python function `flatten(x)` that flattens an arbitrarily nested list of integers into a flat list, keeping the order, e.g. [1,[2,[3]],4] becomes [1,2,3,4]. Nesting can be up to 5000 levels deep. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: RecursionError: maximum recursion depth exceeded)

- 52 tokens in 12.0s, finish: stop
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

- 76 tokens in 21.6s, finish: stop
- verifier: FAIL: flatten([[1],[2,[3]]]) returned [2, 3, 1], expected [1,2,3]

```python
def flatten(x):
    result = []
    stack = [(0, x)]
    while stack:
        start, lst = stack.pop()
        for item in lst:
            if isinstance(item, list):
                stack.append((start, item))
            else:
                result.append(item)
    return result
```

## Attempt 3: FAIL (hidden: AssertionError)

- 76 tokens in 25.3s, finish: stop
- verifier: FAIL: flatten([[1],[2,[3]]]) returned [2, 3, 1], expected [1,2,3]

```python
def flatten(x):
    result = []
    stack = [(0, x)]
    while stack:
        start, lst = stack.pop()
        for item in lst:
            if isinstance(item, list):
                stack.append((start, item))
            else:
                result.append(item)
    return result
```
