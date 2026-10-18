# gemma-4-e4b-concise / py-flatten / seed 43 / naked

## Prompt

Write a Python function `flatten(x)` that flattens an arbitrarily nested list of integers into a flat list, keeping the order, e.g. [1,[2,[3]],4] becomes [1,2,3,4]. Nesting can be up to 5000 levels deep. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: RecursionError: maximum recursion depth exceeded)

- 56 tokens in 12.2s, finish: stop

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
