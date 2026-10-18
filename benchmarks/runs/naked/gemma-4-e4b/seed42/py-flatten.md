# gemma-4-e4b / py-flatten / seed 42 / naked

## Prompt

Write a Python function `flatten(x)` that flattens an arbitrarily nested list of integers into a flat list, keeping the order, e.g. [1,[2,[3]],4] becomes [1,2,3,4]. Nesting can be up to 5000 levels deep. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: RecursionError: maximum recursion depth exceeded)

- 483 tokens in 72.9s, finish: stop

```python
def flatten(x):
    """
    Flattens an arbitrarily nested list of integers into a flat list, 
    keeping the order.
    """
    result = []
    if isinstance(x, list):
        for item in x:
            result.extend(flatten(item))
    else:
        # Assuming the elements are integers as per the problem description
        result.append(x)
    return result

if __name__ == '__main__':
    # Example usage and testing
    test_cases = [
        ([1, [2, [3]], 4], [1, 2, 3, 4]),
        ([1, 2, 3], [1, 2, 3]),
        ([], []),
        ([1], [1]),
        ([[[[1]]]], [1]),
        ([1, [2, [3, [4]]], 5], [1, 2, 3, 4, 5])
    ]

    for input_list, expected_output in test_cases:
        actual_output = flatten(input_list)
        assert actual_output == expected_output, f"Input: {input_list}, Expected: {expected_output}, Got: {actual_output}"
        print(f"Test passed for input: {input_list}")

    # Deep nesting test (up to 5000 levels)
    deep_nesting_list = [1]
    current_list = deep_nesting_list
    for i in range(5000):
        current_list = [current_list]
    
    deep_nesting_list = [1]
    for _ in range(5000):
        deep_nesting_list = [deep_nesting_list]

    print("\nTesting deep nesting...")
    actual_deep = flatten(deep_nesting_list)
    # The expected result is [1] after flattening 5000 levels of nesting around 1
    assert actual_deep == [1], "Deep nesting test failed"
    print("Deep nesting test passed.")
```
