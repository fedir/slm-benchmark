# gemma-4-e4b / py-twosum / seed 43 / naked

## Prompt

Write a Python function `two_sum(nums, target)` returning the two indices [i, j] with i < j whose values add up to `target`; exactly one such pair exists. It is tested with 200000 numbers, so it must be O(n). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 225 tokens in 36.8s, finish: stop

```python
def two_sum(nums, target):
    """
    Finds the indices of two numbers in the list that add up to the target.

    Args:
        nums: A list of integers.
        target: The target sum.

    Returns:
        A list [i, j] of the two indices such that nums[i] + nums[j] == target and i < j.
    """
    num_map = {}  # Dictionary to store {value: index}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            # Found the pair. num_map[complement] is the index of the complement (i < j)
            return [num_map[complement], i]
        
        # Store the current number and its index
        num_map[num] = i

    # According to the problem statement, exactly one such pair exists, so this line should not be reached.
    return []
```
