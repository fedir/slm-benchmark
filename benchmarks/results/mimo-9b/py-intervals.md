# mimo-9b / py-intervals

- category: python
- result: **PASS** (tests passed (no code fence))
- tokens: 104 in 32s (3.3 t/s), finish: stop

## Prompt

Write a Python function `merge_intervals(intervals)` that takes a list of [start, end] pairs and returns the merged list of non-overlapping intervals sorted by start (intervals that touch, like [1,2] and [2,3], must be merged). Reply with ONLY the code in one code block.

## Answer

def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda interval: interval[0])
    merged = [list(intervals[0])]
    for start, end in intervals[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])
    return merged
