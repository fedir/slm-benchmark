# qwen2.5-coder-7b / py-intervals / seed 44 / harness

## Prompt

Write a Python function `merge_intervals(intervals)` that takes a list of [start, end] pairs and returns the merged list of non-overlapping intervals sorted by start (intervals that touch, like [1,2] and [2,3], must be merged). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 125 tokens in 27.7s, finish: stop
- verifier: pass

```python
def merge_intervals(intervals):
    if not intervals:
        return []
    
    # Sort intervals based on the start time
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    for current in intervals[1:]:
        last_merged = merged[-1]
        if current[0] <= last_merged[1]:
            # Merge overlapping intervals
            merged[-1][1] = max(last_merged[1], current[1])
        else:
            # Add new non-overlapping interval
            merged.append(current)
    
    return merged
```
