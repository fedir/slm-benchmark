# nemotron-3-nano-4b / py-flatten / seed 45 / harness

## Prompt

Write a Python function `flatten(x)` that flattens an arbitrarily nested list of integers into a flat list, keeping the order, e.g. [1,[2,[3]],4] becomes [1,2,3,4]. Nesting can be up to 5000 levels deep. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: RecursionError: maximum recursion depth exceeded)

- 45 tokens in 9.0s, finish: stop
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

- 62 tokens in 13.4s, finish: stop
- verifier: FAIL: flatten([[1],[2,[3]]]) returned [[2, [3]], [1], [3], 2, 3, 3, 2, 1, 1], expected [1,2,3]; flatten([[[[9]]]]) returned [[[[9]]], [[9]], [9], 9, 9], expected [9]

```python
def flatten(x):
    result = []
    stack = [x]
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            result.extend(current[::-1])
            stack.extend(current)
        else:
            result.append(current)
    return result
```

## Attempt 3: PASS (hidden: tests passed)

- 63 tokens in 16.7s, finish: stop
- verifier: pass

```python
def flatten(x):
    result = []
    stack = [x]
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            for item in current[::-1]:
                stack.append(item)
        else:
            result.append(current)
    return result
```
