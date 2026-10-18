# gemma-4-e4b / py-intervals / seed 43 / naked

## Prompt

Write a Python function `merge_intervals(intervals)` that takes a list of [start, end] pairs and returns the merged list of non-overlapping intervals sorted by start (intervals that touch, like [1,2] and [2,3], must be merged). Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 313 tokens in 50.0s, finish: stop

```python
def merge_intervals(intervals):
    """
    Merges overlapping intervals in a list of [start, end] pairs.

    Args:
        intervals: A list of intervals, where each interval is [start, end].

    Returns:
        A list of merged, non-overlapping intervals, sorted by start.
    """
    if not intervals:
        return []

    # 1. Sort the intervals based on the start time
    intervals.sort(key=lambda x: x[0])

    merged = []
    # Initialize the current merged interval with the first interval
    current_start, current_end = intervals[0]

    for i in range(1, len(intervals)):
        next_start, next_end = intervals[i]

        # Check for overlap or touching: If the next interval starts before or exactly at the current end
        if next_start <= current_end:
            # Merge: Extend the end of the current interval
            current_end = max(current_end, next_end)
        else:
            # No overlap: Finalize the current merged interval and start a new one
            merged.append([current_start, current_end])
            current_start, current_end = next_start, next_end

    # Append the last processed interval
    merged.append([current_start, current_end])

    return merged
```
