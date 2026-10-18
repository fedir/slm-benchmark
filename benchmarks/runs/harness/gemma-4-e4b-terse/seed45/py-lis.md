# gemma-4-e4b-terse / py-lis / seed 45 / harness

## Prompt

Write a Python function `lis_length(nums)` returning the length of the longest STRICTLY increasing subsequence of a list of integers. It must run in O(n log n) (it will be tested with 200000 elements). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 82 tokens in 16.0s, finish: stop
- verifier: pass

```python
def lis_length(nums):
    tails = []
    for x in nums:
        import bisect
        i = bisect.bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)
```
