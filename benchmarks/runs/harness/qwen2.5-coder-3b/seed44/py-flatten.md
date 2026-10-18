# qwen2.5-coder-3b / py-flatten / seed 44 / harness

## Prompt

Write a Python function `flatten(x)` that flattens an arbitrarily nested list of integers into a flat list, keeping the order, e.g. [1,[2,[3]],4] becomes [1,2,3,4]. Nesting can be up to 5000 levels deep. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: RecursionError: maximum recursion depth exceeded)

- 45 tokens in 6.4s, finish: stop
- verifier: FAIL: the performance example raised RecursionError: maximum recursion depth exceeded

```python
def flatten(x):
    def helper(y):
        if isinstance(y, list):
            return [z for l in y for z in helper(l)]
        return [y]
    return helper(x)
```

## Attempt 2: FAIL (hidden: AssertionError)

- 56 tokens in 8.1s, finish: stop
- verifier: FAIL: flatten([[1],[2,[3]]]) returned [3, 2, 1], expected [1,2,3]

```python
def flatten(x):
    stack = [x]
    flat_list = []
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            stack.extend(current)
        else:
            flat_list.append(current)
    return flat_list
```

## Attempt 3: PASS (hidden: tests passed)

- 62 tokens in 10.3s, finish: stop
- verifier: pass

```python
def flatten(x):
    result = []
    stack = [x]
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            stack.extend(reversed(current))  # Reverse to maintain order
        else:
            result.append(current)
    return result
```
