# qwen2.5-coder-3b / py-intervals / seed 42 / harness

## Prompt

Write a Python function `merge_intervals(intervals)` that takes a list of [start, end] pairs and returns the merged list of non-overlapping intervals sorted by start (intervals that touch, like [1,2] and [2,3], must be merged). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 134 tokens in 13.3s, finish: stop
- verifier: pass

```python
def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort intervals based on the start of each interval
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = merged[-1][1]
        if start <= last_end:
            # Merge if the current interval overlaps with the last merged interval
            merged[-1][1] = max(last_end, end)
        else:
            # Otherwise, add the new interval to the merged list
            merged.append([start, end])

    return merged
```
