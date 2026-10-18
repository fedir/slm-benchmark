# qwen2.5-coder-3b / py-intervals / seed 43 / resample (no feedback)

## Prompt

Write a Python function `merge_intervals(intervals)` that takes a list of [start, end] pairs and returns the merged list of non-overlapping intervals sorted by start (intervals that touch, like [1,2] and [2,3], must be merged). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 134 tokens in 13.4s, finish: stop
- verifier: pass

```python
def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort intervals by their start value
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        last_merged = merged[-1]

        # If current interval overlaps with the last merged interval
        if current[0] <= last_merged[1]:
            # Merge the intervals
            last_merged[1] = max(last_merged[1], current[1])
        else:
            # Add the current interval to the merged list
            merged.append(current)

    return merged
```
