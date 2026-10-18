# qwen2.5-coder-7b / py-lis / seed 42 / harness

## Prompt

Write a Python function `lis_length(nums)` returning the length of the longest STRICTLY increasing subsequence of a list of integers. It must run in O(n log n) (it will be tested with 200000 elements). Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: NameError: name 'bisect' is not defined. Did you forget to import 'bisect'?)

- 73 tokens in 18.2s, finish: stop
- verifier: FAIL: lis_length([0,1,0,3,2,3]) raised NameError: name 'bisect' is not defined; lis_length([5,4,3]) raised NameError: name 'bisect' is not defined; lis_length([2,2,2,2]) raised NameError: name 'bisect' is not defined; the performance example raised NameError: name 'bisect' is not defined

```python
def lis_length(nums):
    if not nums:
        return 0
    tails = []
    for num in nums:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    return len(tails)
```

## Attempt 2: PASS (hidden: tests passed)

- 77 tokens in 22.8s, finish: stop
- verifier: pass

```python
import bisect

def lis_length(nums):
    if not nums:
        return 0
    tails = []
    for num in nums:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    return len(tails)
```
