# mimo-9b / py-flatten / seed 42 / harness

## Prompt

Write a Python function `flatten(x)` that flattens an arbitrarily nested list of integers into a flat list, keeping the order, e.g. [1,[2,[3]],4] becomes [1,2,3,4]. Nesting can be up to 5000 levels deep. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: RecursionError: maximum recursion depth exceeded (no code fence))

- 55 tokens in 18.2s, finish: stop
- verifier: FAIL: the performance example raised RecursionError: maximum recursion depth exceeded

def flatten(x):
    result = []

    def recurse(item):
        if isinstance(item, list):
            for sub in item:
                recurse(sub)
        else:
            result.append(item)

    recurse(x)
    return result

## Attempt 2: PASS (hidden: tests passed (no code fence))

- 59 tokens in 22.8s, finish: stop
- verifier: pass

def flatten(x):
    result = []
    stack = [x]

    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(reversed(item))
        else:
            result.append(item)

    return result
