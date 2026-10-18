# mimo-9b / py-lis / seed 42 / resample (no feedback)

## Prompt

Write a Python function `lis_length(nums)` returning the length of the longest STRICTLY increasing subsequence of a list of integers. It must run in O(n log n) (it will be tested with 200000 elements). Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: NameError: name 'bisect' is not defined. Did you forget to import 'bisect'? (no code fence))

- 110 tokens in 32.2s, finish: stop
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

## Attempt 2: FAIL (hidden: NameError: name 'bisect_left' is not defined (no code fence))

- 88 tokens in 27.3s, finish: stop
- verifier: FAIL: lis_length([0,1,0,3,2,3]) raised NameError: name 'bisect_left' is not defined; lis_length([5,4,3]) raised NameError: name 'bisect_left' is not defined; lis_length([2,2,2,2]) raised NameError: name 'bisect_left' is not defined; the performance example raised NameError: name 'bisect_left' is not defined

def lis_length(nums):
    if not nums:
        return 0

    tails = []
    lengths = []

    for num in nums:
        idx = bisect_left(tails, num)
        if idx == len(tails):
            tails.append(num)
        else:
            tails[idx] = num
        lengths.append(idx + 1)

    return max(lengths)

## Attempt 3: FAIL (hidden: NameError: name 'bisect_left' is not defined (no code fence))

- 114 tokens in 33.4s, finish: stop
- verifier: FAIL: lis_length([0,1,0,3,2,3]) raised NameError: name 'bisect_left' is not defined; lis_length([5,4,3]) raised NameError: name 'bisect_left' is not defined; lis_length([2,2,2,2]) raised NameError: name 'bisect_left' is not defined; the performance example raised NameError: name 'bisect_left' is not defined

def lis_length(nums):
    if not nums:
        return 0

    tails = []
    end_index = []
    length = 0

    for num in nums:
        i = bisect_left(tails, num)
        if i == length:
            tails.append(num)
            end_index.append(len(tails) - 1)
            length += 1
        else:
            tails[i] = num
            end_index[i] = len(end_index) - 1

    return length
