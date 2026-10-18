# qwen2.5-coder-7b / py-lis / seed 43 / resample (no feedback)

## Prompt

Write a Python function `lis_length(nums)` returning the length of the longest STRICTLY increasing subsequence of a list of integers. It must run in O(n log n) (it will be tested with 200000 elements). Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: NameError: name 'bisect' is not defined. Did you forget to import 'bisect'?)

- 73 tokens in 21.3s, finish: stop
- verifier: FAIL: lis_length([0,1,0,3,2,3]) raised NameError: name 'bisect' is not defined; lis_length([5,4,3]) raised NameError: name 'bisect' is not defined; lis_length([2,2,2,2]) raised NameError: name 'bisect' is not defined; the performance example raised NameError: name 'bisect' is not defined

```python
def lis_length(nums):
    if not nums:
        return 0
    tails = []
    for num in nums:
        i = bisect.bisect_left(tails, num)
        if i == len(tails):
            tails.append(num)
        else:
            tails[i] = num
    return len(tails)
```

## Attempt 2: PASS (hidden: tests passed)

- 113 tokens in 26.2s, finish: stop
- verifier: pass

```python
def lis_length(nums):
    if not nums:
        return 0
    tails = []
    for num in nums:
        left, right = 0, len(tails)
        while left < right:
            mid = (left + right) // 2
            if tails[mid] < num:
                left = mid + 1
            else:
                right = mid
        if left == len(tails):
            tails.append(num)
        else:
            tails[left] = num
    return len(tails)
```
