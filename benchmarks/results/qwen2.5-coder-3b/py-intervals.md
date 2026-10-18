# qwen2.5-coder-3b / py-intervals

- category: python
- result: **PASS** (tests passed)
- tokens: 125 in 13s (9.8 t/s), finish: stop

## Prompt

Write a Python function `merge_intervals(intervals)` that takes a list of [start, end] pairs and returns the merged list of non-overlapping intervals sorted by start (intervals that touch, like [1,2] and [2,3], must be merged). Reply with ONLY the code in one code block.

## Answer

```python
def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort intervals by the start value
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for interval in intervals[1:]:
        last_end = merged[-1][1]

        if interval[0] <= last_end:
            # Merge if there's overlap
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            # Otherwise, add the new interval
            merged.append(interval)

    return merged
```
