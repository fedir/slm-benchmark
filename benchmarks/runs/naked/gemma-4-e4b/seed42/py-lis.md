# gemma-4-e4b / py-lis / seed 42 / naked

## Prompt

Write a Python function `lis_length(nums)` returning the length of the longest STRICTLY increasing subsequence of a list of integers. It must run in O(n log n) (it will be tested with 200000 elements). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 259 tokens in 40.1s, finish: stop

```python
import bisect

def lis_length(nums):
    """
    Returns the length of the longest strictly increasing subsequence of a list of integers.
    Runs in O(n log n) time.
    """
    tails = []  # tails[i] is the smallest tail of all increasing subsequences of length i+1

    for num in nums:
        # Find the smallest tail that is >= num
        # bisect_left returns an insertion point which comes before (to the left of)
        # any existing entries of 'num'. If all elements are smaller than 'num',
        # it returns len(tails).
        i = bisect.bisect_left(tails, num)

        if i == len(tails):
            # 'num' is larger than all current tails, so it extends the longest
            # subsequence found so far.
            tails.append(num)
        else:
            # 'num' can potentially start a new subsequence of length i+1 with a
            # smaller tail than tails[i]. We update tails[i] to num.
            tails[i] = num

    return len(tails)
```
