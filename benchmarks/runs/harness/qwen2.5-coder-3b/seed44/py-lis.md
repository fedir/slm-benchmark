# qwen2.5-coder-3b / py-lis / seed 44 / harness

## Prompt

Write a Python function `lis_length(nums)` returning the length of the longest STRICTLY increasing subsequence of a list of integers. It must run in O(n log n) (it will be tested with 200000 elements). Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: NameError: name 'bisect' is not defined. Did you forget to import 'bisect'?)

- 155 tokens in 14.8s, finish: stop
- verifier: FAIL: lis_length([0,1,0,3,2,3]) raised NameError: name 'bisect' is not defined; lis_length([5,4,3]) raised NameError: name 'bisect' is not defined; lis_length([2,2,2,2]) raised NameError: name 'bisect' is not defined; the performance example raised NameError: name 'bisect' is not defined

```python
def lis_length(nums):
    if not nums:
        return 0

    # Initialize a list to store the smallest tail of all increasing subsequences
    tails = [nums[0]]
    
    for num in nums[1:]:
        # Find the position in the tails list where num can be placed
        index = bisect.bisect_left(tails, num)
        
        # If num is greater than any element in tails, append it
        if index == len(tails):
            tails.append(num)
        else:
            # Otherwise, replace the element at index with num
            tails[index] = num
    
    # The length of tails is the length of the longest increasing subsequence
    return len(tails)
```

## Attempt 2: PASS (hidden: tests passed)

- 159 tokens in 17.9s, finish: stop
- verifier: pass

```python
import bisect

def lis_length(nums):
    if not nums:
        return 0

    # Initialize a list to store the smallest tail of all increasing subsequences
    tails = [nums[0]]
    
    for num in nums[1:]:
        # Find the position in the tails list where num can be placed
        index = bisect.bisect_left(tails, num)
        
        # If num is greater than any element in tails, append it
        if index == len(tails):
            tails.append(num)
        else:
            # Otherwise, replace the element at index with num
            tails[index] = num
    
    # The length of tails is the length of the longest increasing subsequence
    return len(tails)
```
