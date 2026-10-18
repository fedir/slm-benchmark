# qwen2.5-coder-7b / py-lis / seed 44 / harness

## Prompt

Write a Python function `lis_length(nums)` returning the length of the longest STRICTLY increasing subsequence of a list of integers. It must run in O(n log n) (it will be tested with 200000 elements). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 115 tokens in 25.7s, finish: stop
- verifier: pass

```python
def lis_length(nums):
    if not nums:
        return 0
    
    tails = []
    
    for num in nums:
        left, right = 0, len(tails)
        
        while left < right:
            mid = (left + right) // 2
            if tails[mid] >= num:
                right = mid
            else:
                left = mid + 1
        
        if left == len(tails):
            tails.append(num)
        else:
            tails[left] = num
    
    return len(tails)
```
