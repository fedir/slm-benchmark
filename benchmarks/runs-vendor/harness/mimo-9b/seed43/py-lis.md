# mimo-9b / py-lis / seed 43 / harness

## Prompt

Write a Python function `lis_length(nums)` returning the length of the longest STRICTLY increasing subsequence of a list of integers. It must run in O(n log n) (it will be tested with 200000 elements). Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: NameError: name 'bisect' is not defined. Did you forget to import 'bisect'? (no code fence))

- 132 tokens in 37.8s, finish: stop
- verifier: FAIL: lis_length([0,1,0,3,2,3]) raised NameError: name 'bisect' is not defined; lis_length([5,4,3]) raised NameError: name 'bisect' is not defined; lis_length([2,2,2,2]) raised NameError: name 'bisect' is not defined; the performance example raised NameError: name 'bisect' is not defined

def lis_length(nums):
    if not nums:
        return 0

    tails = []
    lengths = []

    for num in nums:
        if len(tails) == 0:
            tails.append(num)
            lengths.append(1)
            continue

        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
            lengths.append(lengths[-1] + 1)
        else:
            tails[pos] = num
            lengths[pos] = pos + 1

    return lengths[-1]

## Attempt 2: PASS (hidden: tests passed (no code fence))

- 136 tokens in 46.6s, finish: stop
- verifier: pass

import bisect

def lis_length(nums):
    if not nums:
        return 0

    tails = []
    lengths = []

    for num in nums:
        if len(tails) == 0:
            tails.append(num)
            lengths.append(1)
            continue

        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
            lengths.append(lengths[-1] + 1)
        else:
            tails[pos] = num
            lengths[pos] = pos + 1

    return lengths[-1]
