# mimo-9b / py-lis

- category: python
- result: **FAIL** (NameError: name 'bisect' is not defined. Did you forget to import 'bisect'? (no code fence))
- tokens: 110 in 34s (3.2 t/s), finish: stop

## Prompt

Write a Python function `lis_length(nums)` returning the length of the longest STRICTLY increasing subsequence of a list of integers. It must run in O(n log n) (it will be tested with 200000 elements). Reply with ONLY the code in one code block.

## Answer

def lis_length(nums):
    if not nums:
        return 0

    tails = []
    lengths = []

    for num in nums:
        idx = bisect.bisect_left(tails, num)
        if idx == len(tails):
            tails.append(num)
        else:
            tails[idx] = num
        lengths[idx] = lengths[idx - 1] + 1 if idx > 0 else 1

    return max(lengths) if lengths else 0
