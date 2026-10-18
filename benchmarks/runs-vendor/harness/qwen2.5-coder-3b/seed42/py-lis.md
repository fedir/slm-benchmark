# qwen2.5-coder-3b / py-lis / seed 42 / harness

## Prompt

Write a Python function `lis_length(nums)` returning the length of the longest STRICTLY increasing subsequence of a list of integers. It must run in O(n log n) (it will be tested with 200000 elements). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 185 tokens in 17.7s, finish: stop
- verifier: pass

```python
def lis_length(nums):
    if not nums:
        return 0

    # Initialize a list to store the smallest possible end of all increasing subsequences
    tails = [nums[0]]

    for num in nums[1:]:
        # Binary search to find the position to replace or insert
        left, right = 0, len(tails) - 1
        while left <= right:
            mid = (left + right) // 2
            if tails[mid] < num:
                left = mid + 1
            else:
                right = mid - 1

        # If the number is greater than all elements in tails, append it
        if left == len(tails):
            tails.append(num)
        else:
            # Replace the smallest element greater than or equal to num
            tails[left] = num

    return len(tails)
```
