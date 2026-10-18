# qwen2.5-coder-3b / py-lis / seed 44 / harness

## Prompt

Write a Python function `lis_length(nums)` returning the length of the longest STRICTLY increasing subsequence of a list of integers. It must run in O(n log n) (it will be tested with 200000 elements). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 224 tokens in 21.2s, finish: stop
- verifier: pass

```python
def lis_length(nums):
    if not nums:
        return 0

    # Initialize the list to store the smallest possible end of all increasing subsequences of different lengths
    tails = [nums[0]]
    
    for num in nums[1:]:
        # Binary search to find the position to replace or insert num
        left, right = 0, len(tails) - 1
        while left <= right:
            mid = (left + right) // 2
            if tails[mid] < num:
                left = mid + 1
            else:
                right = mid - 1
        # If num is greater than all elements in tails, append it
        if left == len(tails):
            tails.append(num)
        else:
            # Otherwise, replace the element at left with num
            tails[left] = num
    
    return len(tails)
```

This function implements a binary search to maintain the smallest possible end of all increasing subsequences of different lengths. It runs in O(n log n) time complexity, as required.
