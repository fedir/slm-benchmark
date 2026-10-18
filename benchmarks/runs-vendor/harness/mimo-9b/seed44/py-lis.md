# mimo-9b / py-lis / seed 44 / harness

## Prompt

Write a Python function `lis_length(nums)` returning the length of the longest STRICTLY increasing subsequence of a list of integers. It must run in O(n log n) (it will be tested with 200000 elements). Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: NameError: name 'bisect_left' is not defined (no code fence))

- 108 tokens in 33.3s, finish: stop
- verifier: FAIL: lis_length([0,1,0,3,2,3]) raised NameError: name 'bisect_left' is not defined; lis_length([5,4,3]) raised NameError: name 'bisect_left' is not defined; lis_length([2,2,2,2]) raised NameError: name 'bisect_left' is not defined; the performance example raised NameError: name 'bisect_left' is not defined

def lis_length(nums):
    if not nums:
        return 0

    tails = []  # tails[i] = smallest tail of all increasing subsequences of length i+1
    size = 0
    for num in nums:
        pos = bisect_left(tails, num)  # strictly increasing: never extend equal tails
        if pos == size:
            tails.append(num)
            size += 1
        else:
            tails[pos] = num
    return size

## Attempt 2: FAIL (hidden: NameError: name 'bisect_left' is not defined (no code fence))

- 108 tokens in 47.7s, finish: stop
- verifier: FAIL: lis_length([0,1,0,3,2,3]) raised NameError: name 'bisect_left' is not defined; lis_length([5,4,3]) raised NameError: name 'bisect_left' is not defined; lis_length([2,2,2,2]) raised NameError: name 'bisect_left' is not defined; the performance example raised NameError: name 'bisect_left' is not defined

def lis_length(nums):
    if not nums:
        return 0

    tails = []  # tails[i] = smallest tail of all increasing subsequences of length i+1
    size = 0
    for num in nums:
        pos = bisect_left(tails, num)  # strictly increasing: never extend equal tails
        if pos == size:
            tails.append(num)
            size += 1
        else:
            tails[pos] = num
    return size

## Attempt 3: PASS (hidden: tests passed (no code fence))

- 115 tokens in 58.0s, finish: stop
- verifier: pass

import bisect

def lis_length(nums):
    if not nums:
        return 0

    tails = []  # tails[i] = smallest tail of all increasing subsequences of length i+1
    size = 0
    for num in nums:
        pos = bisect.bisect_left(tails, num)  # strictly increasing: never extend equal tails
        if pos == size:
            tails.append(num)
            size += 1
        else:
            tails[pos] = num
    return size
