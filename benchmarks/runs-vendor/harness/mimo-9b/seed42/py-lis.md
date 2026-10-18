# mimo-9b / py-lis / seed 42 / harness

## Prompt

Write a Python function `lis_length(nums)` returning the length of the longest STRICTLY increasing subsequence of a list of integers. It must run in O(n log n) (it will be tested with 200000 elements). Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: NameError: name 'bisect' is not defined. Did you forget to import 'bisect'? (no code fence))

- 110 tokens in 35.6s, finish: stop
- verifier: FAIL: lis_length([0,1,0,3,2,3]) raised NameError: name 'bisect' is not defined; lis_length([5,4,3]) raised NameError: name 'bisect' is not defined; lis_length([2,2,2,2]) raised NameError: name 'bisect' is not defined; the performance example raised NameError: name 'bisect' is not defined

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

## Attempt 2: FAIL (hidden: IndexError: list assignment index out of range (no code fence))

- 115 tokens in 44.5s, finish: stop
- verifier: FAIL: lis_length([0,1,0,3,2,3]) raised IndexError: list assignment index out of range; lis_length([5,4,3]) raised IndexError: list assignment index out of range; lis_length([2,2,2,2]) raised IndexError: list assignment index out of range; the performance example raised IndexError: list assignment index out of range

def lis_length(nums):
    import bisect

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

## Attempt 3: FAIL (hidden: AssertionError (no code fence))

- 125 tokens in 57.9s, finish: stop
- verifier: FAIL: lis_length([5,4,3]) returned 3, expected 1; lis_length([2,2,2,2]) returned 4, expected 1

def lis_length(nums):
    import bisect

    if not nums:
        return 0

    tails = []
    lengths = []

    for num in nums:
        idx = bisect.bisect_left(tails, num)
        if idx == len(tails):
            tails.append(num)
            lengths.append(lengths[-1] + 1 if lengths else 1)
        else:
            tails[idx] = num
            lengths[idx] = lengths[idx - 1] + 1

    return max(lengths) if lengths else 0
