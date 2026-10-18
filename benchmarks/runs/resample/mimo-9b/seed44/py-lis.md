# mimo-9b / py-lis / seed 44 / resample (no feedback)

## Prompt

Write a Python function `lis_length(nums)` returning the length of the longest STRICTLY increasing subsequence of a list of integers. It must run in O(n log n) (it will be tested with 200000 elements). Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: NameError: name 'bisect_left' is not defined (no code fence))

- 108 tokens in 31.7s, finish: stop
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

## Attempt 2: FAIL (hidden: NameError: name 'bisect' is not defined. Did you forget to import 'bisect'? (no code fence))

- 80 tokens in 25.5s, finish: stop
- verifier: FAIL: lis_length([0,1,0,3,2,3]) raised NameError: name 'bisect' is not defined; lis_length([5,4,3]) raised NameError: name 'bisect' is not defined; lis_length([2,2,2,2]) raised NameError: name 'bisect' is not defined; the performance example raised NameError: name 'bisect' is not defined

def lis_length(nums):
    if not nums:
        return 0
    tails = []
    for num in nums:
        if not tails or num > tails[-1]:
            tails.append(num)
        else:
            idx = bisect.bisect_left(tails, num)
            tails[idx] = num
    return len(tails)

## Attempt 3: FAIL (hidden: NameError: name 'bisect' is not defined. Did you forget to import 'bisect'? (no code fence))

- 90 tokens in 27.6s, finish: stop
- verifier: FAIL: lis_length([0,1,0,3,2,3]) raised NameError: name 'bisect' is not defined; lis_length([5,4,3]) raised NameError: name 'bisect' is not defined; lis_length([2,2,2,2]) raised NameError: name 'bisect' is not defined; the performance example raised NameError: name 'bisect' is not defined

def lis_length(nums):
    if not nums:
        return 0

    tails = []
    lengths = []

    for num in nums:
        i = bisect.bisect_left(tails, num)
        if i == len(tails):
            tails.append(num)
        else:
            tails[i] = num

        lengths.append(len(tails))

    return max(lengths)
