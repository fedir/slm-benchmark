# nemotron-3-nano-4b / py-intervals / seed 44 / resample (no feedback)

## Prompt

Write a Python function `merge_intervals(intervals)` that takes a list of [start, end] pairs and returns the merged list of non-overlapping intervals sorted by start (intervals that touch, like [1,2] and [2,3], must be merged). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 97 tokens in 15.9s, finish: stop
- verifier: pass

```python
def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for cur in intervals[1:]:
        last = merged[-1]
        if cur[0] <= last[1]:
            merged[-1][1] = max(last[1], cur[1])
        else:
            merged.append(cur)
    return merged
```
