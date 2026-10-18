# ornith-9b-mtp / py-intervals / seed 44 / harness

## Prompt

Write a Python function `merge_intervals(intervals)` that takes a list of [start, end] pairs and returns the merged list of non-overlapping intervals sorted by start (intervals that touch, like [1,2] and [2,3], must be merged). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 161 tokens in 31.9s, finish: stop
- verifier: pass

```python
def merge_intervals(intervals):
    if not intervals:
        return []
    
    # Sort intervals by start time
    intervals = sorted(intervals, key=lambda x: x[0])
    
    merged = [list(intervals[0])]
    
    for start, end in intervals[1:]:
        last_start, last_end = merged[-1]
        
        # Merge if current interval overlaps or touches previous one
        if start <= last_end:
            # Extend the previous interval's end if needed
            merged[-1] = [last_start, max(last_end, end)]
        else:
            # No overlap, add a new interval
            merged.append([start, end])
    
    return merged
```
