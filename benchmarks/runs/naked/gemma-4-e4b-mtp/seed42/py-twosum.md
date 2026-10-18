# gemma-4-e4b-mtp / py-twosum / seed 42 / naked

## Prompt

Write a Python function `two_sum(nums, target)` returning the two indices [i, j] with i < j whose values add up to `target`; exactly one such pair exists. It is tested with 200000 numbers, so it must be O(n). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 226 tokens in 29.0s, finish: stop

```python
def two_sum(nums, target):
    """
    Finds the indices of two numbers in the list 'nums' that add up to 'target'.

    Args:
        nums (list[int]): The list of numbers.
        target (int): The target sum.

    Returns:
        list[int]: A list containing the two indices [i, j] where i < j.
    """
    num_map = {}  # Dictionary to store {value: index}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            # Found the pair. Since we iterate in increasing order of i,
            # num_map[complement]'s index will be less than i.
            return [num_map[complement], i]
        num_map[num] = i
    # According to the problem description, exactly one such pair exists,
    # so this return should theoretically not be reached.
    return []
```
