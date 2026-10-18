# gemma-4-e4b / py-twosum / seed 42 / naked

## Prompt

Write a Python function `two_sum(nums, target)` returning the two indices [i, j] with i < j whose values add up to `target`; exactly one such pair exists. It is tested with 200000 numbers, so it must be O(n). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 252 tokens in 39.1s, finish: stop

```python
def two_sum(nums, target):
    """
    Finds the indices of two numbers in the list whose values add up to the target.

    Args:
        nums: A list of integers.
        target: The target sum.

    Returns:
        A list containing the two indices [i, j] such that nums[i] + nums[j] == target and i < j.
    """
    num_map = {}  # Dictionary to store {value: index}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            # Found the pair: the current index i and the index of the complement stored in the map
            # Since we iterate in increasing order of i, the index stored in num_map will be less than i.
            return [num_map[complement], i]
        
        # Store the current number and its index
        num_map[num] = i
    
    # As per the problem description, exactly one such pair exists, so this line should ideally not be reached.
    return [] 
```
