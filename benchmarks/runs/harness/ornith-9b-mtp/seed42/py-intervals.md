# ornith-9b-mtp / py-intervals / seed 42 / harness

## Prompt

Write a Python function `merge_intervals(intervals)` that takes a list of [start, end] pairs and returns the merged list of non-overlapping intervals sorted by start (intervals that touch, like [1,2] and [2,3], must be merged). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 111 tokens in 21.8s, finish: stop
- verifier: pass

```python
def merge_intervals(intervals):
    if not intervals:
        return []
    
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [list(intervals[0])]
    
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    
    return merged
```
