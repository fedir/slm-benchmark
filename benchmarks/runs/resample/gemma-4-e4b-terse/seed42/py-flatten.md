# gemma-4-e4b-terse / py-flatten / seed 42 / resample (no feedback)

## Prompt

Write a Python function `flatten(x)` that flattens an arbitrarily nested list of integers into a flat list, keeping the order, e.g. [1,[2,[3]],4] becomes [1,2,3,4]. Nesting can be up to 5000 levels deep. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: RecursionError: maximum recursion depth exceeded)

- 51 tokens in 11.6s, finish: stop
- verifier: FAIL: the performance example raised RecursionError: maximum recursion depth exceeded

```python
def flatten(x):
    if isinstance(x, list):
        return [item for sublist in (flatten(i) for i in x) for item in sublist]
    return [x]
```

## Attempt 2: FAIL (hidden: RecursionError: maximum recursion depth exceeded)

- 51 tokens in 11.5s, finish: stop
- verifier: FAIL: the performance example raised RecursionError: maximum recursion depth exceeded

```python
def flatten(x):
    if isinstance(x, list):
        return [item for sublist in (flatten(item) for item in x) for item in sublist]
    return [x]
```

## Attempt 3: FAIL (hidden: RecursionError: maximum recursion depth exceeded)

- 51 tokens in 11.5s, finish: stop
- verifier: FAIL: the performance example raised RecursionError: maximum recursion depth exceeded

```python
def flatten(x):
    if isinstance(x, list):
        return [item for sublist in (flatten(item) for item in x) for item in sublist]
    return [x]
```
