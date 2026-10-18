# nemotron-3-nano-4b / py-lis / seed 42 / harness

## Prompt

Write a Python function `lis_length(nums)` returning the length of the longest STRICTLY increasing subsequence of a list of integers. It must run in O(n log n) (it will be tested with 200000 elements). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 78 tokens in 13.5s, finish: stop
- verifier: pass

```python
def lis_length(nums):
    import bisect
    if not nums:
        return 0
    tails = []
    for num in nums:
        idx = bisect.bisect_left(tails, num)
        if idx == len(tails):
            tails.append(num)
        else:
            tails[idx] = num
    return len(tails)
```
