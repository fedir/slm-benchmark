# qwen2.5-coder-3b / py-intervals / seed 44 / harness

## Prompt

Write a Python function `merge_intervals(intervals)` that takes a list of [start, end] pairs and returns the merged list of non-overlapping intervals sorted by start (intervals that touch, like [1,2] and [2,3], must be merged). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 125 tokens in 12.3s, finish: stop
- verifier: pass

```python
def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort intervals based on the start time
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            # No overlap, add the current interval to merged
            merged.append(interval)
        else:
            # Overlap, merge the current interval with the last in merged
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged
```
