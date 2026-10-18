# gemma-4-e4b / py-flatten / seed 43 / naked

## Prompt

Write a Python function `flatten(x)` that flattens an arbitrarily nested list of integers into a flat list, keeping the order, e.g. [1,[2,[3]],4] becomes [1,2,3,4]. Nesting can be up to 5000 levels deep. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: RecursionError: maximum recursion depth exceeded)

- 508 tokens in 79.7s, finish: stop

```python
def flatten(x):
    """
    Flattens an arbitrarily nested list of integers into a flat list, keeping the order.
    """
    if isinstance(x, list):
        result = []
        for item in x:
            result.extend(flatten(item))
        return result
    else:
        # If the item is an integer (or any non-list type we want to keep)
        return [x]

if __name__ == '__main__':
    # Example usage:
    test1 = [1, [2, [3]], 4]
    print(f"Input: {test1}, Output: {flatten(test1)}") # Expected: [1, 2, 3, 4]

    test2 = [1, [2, [3, [4]]], 5]
    print(f"Input: {test2}, Output: {flatten(test2)}") # Expected: [1, 2, 3, 4, 5]

    test3 = [[[[1]]], 2]
    print(f"Input: {test3}, Output: {flatten(test3)}") # Expected: [1, 2]

    test4 = [1, 2, 3]
    print(f"Input: {test4}, Output: {flatten(test4)}") # Expected: [1, 2, 3]

    test5 = []
    print(f"Input: {test5}, Output: {flatten(test5)}") # Expected: []

    # Deep nesting test (to check recursion limit safety, although Python's default limit is usually high enough)
    deep_list = [1]
    current = deep_list
    for i in range(5000):
        current.append([i + 2])
    
    print("\nTesting deep nesting (5000 levels)...")
    # The function should handle this without hitting a recursion limit error if the default limit is >= 5001
    try:
        flat_deep = flatten(deep_list)
        print(f"Deep list flattened successfully. Length: {len(flat_deep)}")
    except RecursionError:
        print("RecursionError encountered during deep flattening.")
```
