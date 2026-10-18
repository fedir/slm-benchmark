# qwen2.5-coder-7b / py-flatten / seed 45 / harness

## Prompt

Write a Python function `flatten(x)` that flattens an arbitrarily nested list of integers into a flat list, keeping the order, e.g. [1,[2,[3]],4] becomes [1,2,3,4]. Nesting can be up to 5000 levels deep. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: RecursionError: maximum recursion depth exceeded)

- 52 tokens in 13.5s, finish: stop
- verifier: FAIL: the performance example raised RecursionError: maximum recursion depth exceeded

```python
def flatten(x):
    result = []
    def helper(sublist):
        for item in sublist:
            if isinstance(item, list):
                helper(item)
            else:
                result.append(item)
    helper(x)
    return result
```

## Attempt 2: FAIL (hidden: AssertionError)

- 57 tokens in 17.3s, finish: stop
- verifier: FAIL: flatten([[1],[2,[3]]]) returned [3, 2, 1], expected [1,2,3]

```python
def flatten(x):
    result = []
    stack = [x]
    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(reversed(item))
        else:
            result.append(item)
    return result[::-1]
```

## Attempt 3: FAIL (hidden: AssertionError)

- 58 tokens in 19.1s, finish: stop
- verifier: FAIL: flatten([[1],[2,[3]]]) returned [3, 2, 1], expected [1,2,3]

```python
def flatten(x):
    result = []
    stack = [x]
    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(reversed(item))
        else:
            result.insert(0, item)
    return result
```
