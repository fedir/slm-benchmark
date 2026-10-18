# ornith-9b-mtp / py-lis / seed 44 / harness

## Prompt

Write a Python function `lis_length(nums)` returning the length of the longest STRICTLY increasing subsequence of a list of integers. It must run in O(n log n) (it will be tested with 200000 elements). Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: IndexError: list assignment index out of range)

- 122 tokens in 22.2s, finish: stop
- verifier: FAIL: lis_length([0,1,0,3,2,3]) raised IndexError: list assignment index out of range; lis_length([5,4,3]) raised IndexError: list assignment index out of range; lis_length([2,2,2,2]) raised IndexError: list assignment index out of range; the performance example raised IndexError: list assignment index out of range

```python
def lis_length(nums):
    if not nums:
        return 0
    tails = []
    for x in nums:
        lo, hi = 0, len(tails)
        while lo < hi:
            mid = (lo + hi) // 2
            if tails[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        tails[lo] = x
        if lo == len(tails):
            tails.append(x)
    return len(tails)
```

## Attempt 2: FAIL (hidden: IndexError: list assignment index out of range)

- 122 tokens in 29.1s, finish: stop
- verifier: FAIL: lis_length([0,1,0,3,2,3]) raised IndexError: list assignment index out of range; lis_length([5,4,3]) raised IndexError: list assignment index out of range; lis_length([2,2,2,2]) raised IndexError: list assignment index out of range; the performance example raised IndexError: list assignment index out of range

```python
def lis_length(nums):
    if not nums:
        return 0
    tails = []
    for x in nums:
        lo, hi = 0, len(tails)
        while lo < hi:
            mid = (lo + hi) // 2
            if tails[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        tails[lo] = x
        if lo == len(tails):
            tails.append(x)
    return len(tails)
```

## Attempt 3: FAIL (hidden: IndexError: list assignment index out of range)

- 122 tokens in 37.1s, finish: stop
- verifier: FAIL: lis_length([0,1,0,3,2,3]) raised IndexError: list assignment index out of range; lis_length([5,4,3]) raised IndexError: list assignment index out of range; lis_length([2,2,2,2]) raised IndexError: list assignment index out of range; the performance example raised IndexError: list assignment index out of range

```python
def lis_length(nums):
    if not nums:
        return 0
    tails = []
    for x in nums:
        lo, hi = 0, len(tails)
        while lo < hi:
            mid = (lo + hi) // 2
            if tails[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        tails[lo] = x
        if lo == len(tails):
            tails.append(x)
    return len(tails)
```
