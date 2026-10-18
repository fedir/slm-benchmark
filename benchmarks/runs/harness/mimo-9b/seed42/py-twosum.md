# mimo-9b / py-twosum / seed 42 / harness

## Prompt

Write a Python function `two_sum(nums, target)` returning the two indices [i, j] with i < j whose values add up to `target`; exactly one such pair exists. It is tested with 200000 numbers, so it must be O(n). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed (no code fence))

- 66 tokens in 21.0s, finish: stop
- verifier: pass

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    raise ValueError("No two-sum pair found")
