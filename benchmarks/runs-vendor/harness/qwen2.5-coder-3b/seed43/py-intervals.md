# qwen2.5-coder-3b / py-intervals / seed 43 / harness

## Prompt

Write a Python function `merge_intervals(intervals)` that takes a list of [start, end] pairs and returns the merged list of non-overlapping intervals sorted by start (intervals that touch, like [1,2] and [2,3], must be merged). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 174 tokens in 16.8s, finish: stop
- verifier: pass

```python
def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort intervals based on the start value
    intervals.sort(key=lambda x: x[0])

    # Initialize the result list with the first interval
    merged = [intervals[0]]

    # Iterate through the sorted intervals starting from the second one
    for current in intervals[1:]:
        last_merged = merged[-1]
        
        # Check if the current interval overlaps with the last merged interval
        if current[0] <= last_merged[1]:
            # Merge the intervals by updating the end of the last merged interval
            last_merged[1] = max(last_merged[1], current[1])
        else:
            # If no overlap, add the current interval to the result
            merged.append(current)

    return merged
```
