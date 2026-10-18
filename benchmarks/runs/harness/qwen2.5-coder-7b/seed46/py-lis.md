# qwen2.5-coder-7b / py-lis / seed 46 / harness

## Prompt

Write a Python function `lis_length(nums)` returning the length of the longest STRICTLY increasing subsequence of a list of integers. It must run in O(n log n) (it will be tested with 200000 elements). Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: IndexError: list assignment index out of range)

- 99 tokens in 22.6s, finish: stop
- verifier: FAIL: lis_length([0,1,0,3,2,3]) raised IndexError: list assignment index out of range; lis_length([5,4,3]) raised IndexError: list assignment index out of range; lis_length([2,2,2,2]) raised IndexError: list assignment index out of range; the performance example raised IndexError: list assignment index out of range

```python
def lis_length(nums):
    if not nums:
        return 0
    
    tails = []
    
    for num in nums:
        left, right = 0, len(tails)
        while left < right:
            mid = (left + right) // 2
            if tails[mid] < num:
                left = mid + 1
            else:
                right = mid
        tails[left] = num
    
    return left + 1
```

## Attempt 2: PASS (hidden: tests passed)

- 114 tokens in 30.0s, finish: stop
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
            if tails[mid] < num:
                left = mid + 1
            else:
                right = mid
        if left == len(tails):
            tails.append(num)
        else:
            tails[left] = num
    
    return len(tails)
```
