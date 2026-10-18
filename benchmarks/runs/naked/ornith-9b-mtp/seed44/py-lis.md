# ornith-9b-mtp / py-lis / seed 44 / naked

## Prompt

Write a Python function `lis_length(nums)` returning the length of the longest STRICTLY increasing subsequence of a list of integers. It must run in O(n log n) (it will be tested with 200000 elements). Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: IndexError: list assignment index out of range)

- 122 tokens in 23.8s, finish: stop

```python
def lis_length(nums):
    if not nums:
        return 0
    tails = []
    for x in nums:
        lo, hi = 0, len(tails)
        while lo < hi:
            mid = (lo + hi) // 2
            if tails[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        tails[lo] = x
        if lo == len(tails):
            tails.append(x)
    return len(tails)
```
