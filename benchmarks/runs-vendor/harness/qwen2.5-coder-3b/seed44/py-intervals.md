# qwen2.5-coder-3b / py-intervals / seed 44 / harness

## Prompt

Write a Python function `merge_intervals(intervals)` that takes a list of [start, end] pairs and returns the merged list of non-overlapping intervals sorted by start (intervals that touch, like [1,2] and [2,3], must be merged). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 132 tokens in 13.1s, finish: stop
- verifier: pass

```python
def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort intervals by their start values
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for interval in intervals[1:]:
        # Check if the current interval overlaps with the last merged interval
        if interval[0] <= merged[-1][1]:
            # Merge the intervals
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            # Add the current interval to the merged list
            merged.append(interval)

    return merged
```
