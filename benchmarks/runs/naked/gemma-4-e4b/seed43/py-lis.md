# gemma-4-e4b / py-lis / seed 43 / naked

## Prompt

Write a Python function `lis_length(nums)` returning the length of the longest STRICTLY increasing subsequence of a list of integers. It must run in O(n log n) (it will be tested with 200000 elements). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 288 tokens in 46.4s, finish: stop

```python
import bisect

def lis_length(nums):
    """
    Returns the length of the longest strictly increasing subsequence of a list of integers.
    Uses an O(n log n) approach.
    """
    if not nums:
        return 0

    # tails[i] stores the smallest tail of all increasing subsequences of length i+1.
    # This array will always be sorted.
    tails = []

    for num in nums:
        # Find the first element in 'tails' that is greater than or equal to 'num'.
        # bisect_left finds the insertion point to maintain sorted order.
        i = bisect.bisect_left(tails, num)

        if i == len(tails):
            # 'num' is larger than all existing tails, so it extends the longest 
            # subsequence found so far by 1.
            tails.append(num)
        else:
            # 'num' can potentially start a new subsequence of length i+1 
            # with a smaller tail than the current one (tails[i]).
            # We replace tails[i] with 'num' because a smaller tail is always 
            # better for future extensions.
            tails[i] = num

    return len(tails)
```
