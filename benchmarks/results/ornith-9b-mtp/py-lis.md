# ornith-9b-mtp / py-lis

- category: python
- result: **PASS** (tests passed)
- tokens: 104 in 24s (4.4 t/s), finish: stop

## Prompt

Write a Python function `lis_length(nums)` returning the length of the longest STRICTLY increasing subsequence of a list of integers. It must run in O(n log n) (it will be tested with 200000 elements). Reply with ONLY the code in one code block.

## Answer

```python
import bisect

def lis_length(nums):
    if not nums:
        return 0
    tails = [float('inf')] * (len(nums) + 1)
    size = 0
    for x in nums:
        idx = bisect.bisect_left(tails, x, 0, size + 1)
        tails[idx] = x
        if idx == size:
            size += 1
    return size
```
