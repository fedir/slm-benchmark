# qwen2.5-coder-3b / py-intervals / seed 46 / resample (no feedback)

## Prompt

Write a Python function `merge_intervals(intervals)` that takes a list of [start, end] pairs and returns the merged list of non-overlapping intervals sorted by start (intervals that touch, like [1,2] and [2,3], must be merged). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 137 tokens in 13.4s, finish: stop
- verifier: pass

```python
def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort intervals by their start value
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_merged_end = merged[-1][1]

        if start <= last_merged_end:
            # If the current interval overlaps with the last merged interval, merge them
            merged[-1][1] = max(last_merged_end, end)
        else:
            # If not, add the current interval to the merged list
            merged.append([start, end])

    return merged
```
