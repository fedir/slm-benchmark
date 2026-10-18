# nemotron-3-nano-4b / py-lis

- category: python
- result: **PASS** (tests passed)
- tokens: 68 in 12s (5.6 t/s), finish: stop

## Prompt

Write a Python function `lis_length(nums)` returning the length of the longest STRICTLY increasing subsequence of a list of integers. It must run in O(n log n) (it will be tested with 200000 elements). Reply with ONLY the code in one code block.

## Answer

```python
def lis_length(nums):
    import bisect
    tail = []
    for x in nums:
        i = bisect.bisect_left(tail, x)
        if i == len(tail):
            tail.append(x)
        else:
            tail[i] = x
    return len(tail)
```
