# qwen2.5-coder-3b / py-lis / seed 43 / harness

## Prompt

Write a Python function `lis_length(nums)` returning the length of the longest STRICTLY increasing subsequence of a list of integers. It must run in O(n log n) (it will be tested with 200000 elements). Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: NameError: name 'bisect' is not defined. Did you forget to import 'bisect'?)

- 174 tokens in 16.8s, finish: stop
- verifier: FAIL: lis_length([0,1,0,3,2,3]) raised NameError: name 'bisect' is not defined; lis_length([5,4,3]) raised NameError: name 'bisect' is not defined; lis_length([2,2,2,2]) raised NameError: name 'bisect' is not defined; the performance example raised NameError: name 'bisect' is not defined

```python
def lis_length(nums):
    if not nums:
        return 0

    # Initialize an array to store the smallest tail of all increasing subsequences
    tails = [nums[0]]

    for num in nums[1:]:
        # Use binary search to find the position to replace in tails
        i = bisect.bisect_left(tails, num)
        
        # If num is larger than all elements in tails, append it
        if i == len(tails):
            tails.append(num)
        else:
            tails[i] = num

    return len(tails)

# Example usage:
# nums = [10, 9, 2, 5, 3, 7, 101, 18]
# print(lis_length(nums))  # Output: 4
```

## Attempt 2: PASS (hidden: tests passed)

- 163 tokens in 19.3s, finish: stop
- verifier: pass

```python
import bisect

def lis_length(nums):
    if not nums:
        return 0

    # Initialize an array to store the smallest tail of all increasing subsequences
    tails = [nums[0]]

    for num in nums[1:]:
        # Use binary search to find the position to replace in tails
        i = bisect.bisect_left(tails, num)
        
        # If num is larger than all elements in tails, append it
        if i == len(tails):
            tails.append(num)
        else:
            tails[i] = num

    return len(tails)

# Example usage:
# nums = [0,1,0,3,2,3]
# print(lis_length(nums))  # Output: 4
```
