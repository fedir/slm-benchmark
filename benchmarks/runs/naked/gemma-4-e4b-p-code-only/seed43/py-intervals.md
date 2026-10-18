# gemma-4-e4b-p-code-only / py-intervals / seed 43 / naked

## Prompt

Write a Python function `merge_intervals(intervals)` that takes a list of [start, end] pairs and returns the merged list of non-overlapping intervals sorted by start (intervals that touch, like [1,2] and [2,3], must be merged). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 174 tokens in 29.2s, finish: stop

```python
def merge_intervals(intervals):
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])
    
    merged = []
    current_start, current_end = intervals[0]
    
    for i in range(1, len(intervals)):
        next_start, next_end = intervals[i]
        
        if next_start <= current_end:
            current_end = max(current_end, next_end)
        else:
            merged.append([current_start, current_end])
            current_start, current_end = next_start, next_end
            
    merged.append([current_start, current_end])
    return merged
```
