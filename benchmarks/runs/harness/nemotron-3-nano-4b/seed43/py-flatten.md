# nemotron-3-nano-4b / py-flatten / seed 43 / harness

## Prompt

Write a Python function `flatten(x)` that flattens an arbitrarily nested list of integers into a flat list, keeping the order, e.g. [1,[2,[3]],4] becomes [1,2,3,4]. Nesting can be up to 5000 levels deep. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: RecursionError: maximum recursion depth exceeded)

- 45 tokens in 8.9s, finish: stop
- verifier: FAIL: the performance example raised RecursionError: maximum recursion depth exceeded

```python
def flatten(x):
    result = []
    for element in x:
        if isinstance(element, list):
            result.extend(flatten(element))
        else:
            result.append(element)
    return result
```

## Attempt 2: FAIL (hidden: AssertionError)

- 59 tokens in 13.0s, finish: stop
- verifier: FAIL: flatten([[1],[2,[3]]]) returned [3, 2, 1], expected [1,2,3]

```python
def flatten(x):
    result = []
    stack = [x]
    while stack:
        element = stack.pop()
        if isinstance(element, list):
            stack.extend(reversed(element))
        else:
            result.append(element)
    return result[::-1]
```

## Attempt 3: PASS (hidden: tests passed)

- 57 tokens in 15.0s, finish: stop
- verifier: pass

```python
def flatten(x):
    result = []
    stack = [x]
    while stack:
        element = stack.pop()
        if isinstance(element, list):
            stack.extend(element)
        else:
            result.append(element)
    return result[::-1]
```
