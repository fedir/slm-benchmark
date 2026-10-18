# nemotron-3-nano-4b / py-twosum / seed 45 / resample (no feedback)

## Prompt

Write a Python function `two_sum(nums, target)` returning the two indices [i, j] with i < j whose values add up to `target`; exactly one such pair exists. It is tested with 200000 numbers, so it must be O(n). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 63 tokens in 11.5s, finish: stop
- verifier: pass

```python
def two_sum(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
```
