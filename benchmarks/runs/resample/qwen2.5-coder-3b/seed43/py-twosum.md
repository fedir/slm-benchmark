# qwen2.5-coder-3b / py-twosum / seed 43 / resample (no feedback)

## Prompt

Write a Python function `two_sum(nums, target)` returning the two indices [i, j] with i < j whose values add up to `target`; exactly one such pair exists. It is tested with 200000 numbers, so it must be O(n). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 153 tokens in 15.1s, finish: stop
- verifier: pass

```python
def two_sum(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return None
```
This solution uses a dictionary to keep track of the indices of the numbers we've seen so far. For each number in the list, it calculates the complement needed to reach the target sum. If the complement is already in the dictionary, it means we've found the two numbers that add up to the target, and we return their indices. If not, we add the current number and its index to the dictionary and continue.
