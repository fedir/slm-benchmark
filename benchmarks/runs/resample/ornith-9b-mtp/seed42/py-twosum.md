# ornith-9b-mtp / py-twosum / seed 42 / resample (no feedback)

## Prompt

Write a Python function `two_sum(nums, target)` returning the two indices [i, j] with i < j whose values add up to `target`; exactly one such pair exists. It is tested with 200000 numbers, so it must be O(n). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 74 tokens in 17.3s, finish: stop
- verifier: pass

```python
def two_sum(nums, target):
    index_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in index_map:
            return [index_map[complement], i]
        index_map[num] = i
    raise ValueError("No two sum solution")
```
