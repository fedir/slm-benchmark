# gemma-4-e4b-terse / py-flatten / seed 45 / harness

## Prompt

Write a Python function `flatten(x)` that flattens an arbitrarily nested list of integers into a flat list, keeping the order, e.g. [1,[2,[3]],4] becomes [1,2,3,4]. Nesting can be up to 5000 levels deep. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: RecursionError: maximum recursion depth exceeded)

- 46 tokens in 11.1s, finish: stop
- verifier: FAIL: flatten([[1],[2,[3]]]) raised RecursionError: maximum recursion depth exceeded; flatten([]) raised RecursionError: maximum recursion depth exceeded; flatten([[[[9]]]]) raised RecursionError: maximum recursion depth exceeded; the performance example raised RecursionError: maximum recursion depth exceeded

```python
def flatten(x):
    if isinstance(x, list):
        return [item for sublist in [x] for item in flatten(sublist)]
    return [x]
```

## Attempt 2: FAIL (hidden: AssertionError)

- 72 tokens in 22.3s, finish: stop
- verifier: FAIL: flatten([[1],[2,[3]]]) returned [2, 3, 1], expected [1,2,3]

```python
def flatten(x):
    result = []
    stack = list(x)
    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(item[::-1])
        else:
            result.append(item)
    return result
```

## Attempt 3: PASS (hidden: tests passed)

- 75 tokens in 25.9s, finish: stop
- verifier: pass

```python
def flatten(x):
    result = []
    stack = list(x)[::-1]
    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(item[::-1])
        else:
            result.append(item)
    return result
```
