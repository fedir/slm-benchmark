# gemma-4-e4b-mtp / py-lis / seed 42 / naked

## Prompt

Write a Python function `lis_length(nums)` returning the length of the longest STRICTLY increasing subsequence of a list of integers. It must run in O(n log n) (it will be tested with 200000 elements). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 295 tokens in 37.6s, finish: stop

```python
import bisect

def lis_length(nums):
    """
    Returns the length of the longest strictly increasing subsequence of a list of integers.
    Runs in O(n log n) time.
    """
    if not nums:
        return 0

    # 'tails' will store the smallest tail of all increasing subsequences
    # with length i+1 at index i.
    tails = []

    for num in nums:
        # Find the first element in 'tails' that is greater than or equal to 'num'
        # bisect_left returns the insertion point which comes before (to the left of)
        # any existing entries of 'num'.
        i = bisect.bisect_left(tails, num)

        if i == len(tails):
            # 'num' is greater than all existing tails, so we extend the longest
            # subsequence found so far by appending 'num'.
            tails.append(num)
        else:
            # 'num' can potentially be the end of an increasing subsequence of length i+1
            # with a smaller tail than tails[i]. We update tails[i] to 'num'.
            tails[i] = num

    # The length of 'tails' is the length of the LIS.
    return len(tails)
```
