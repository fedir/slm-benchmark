# gemma-4-e4b-concise / py-intervals / seed 42 / naked

## Prompt

Write a Python function `merge_intervals(intervals)` that takes a list of [start, end] pairs and returns the merged list of non-overlapping intervals sorted by start (intervals that touch, like [1,2] and [2,3], must be merged). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 116 tokens in 20.4s, finish: stop

```python
def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        last_merged = merged[-1]
        if start <= last_merged[1]:
            merged[-1][1] = max(last_merged[1], end)
        else:
            merged.append([start, end])
    return merged
```
