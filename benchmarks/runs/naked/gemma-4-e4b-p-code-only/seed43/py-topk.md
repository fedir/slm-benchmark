# gemma-4-e4b-p-code-only / py-topk / seed 43 / naked

## Prompt

Write a Python function `top_k_frequent(words, k)` returning the k most frequent words as a list, ordered by frequency descending, ties broken alphabetically. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 79 tokens in 14.8s, finish: stop

```python
from collections import Counter

def top_k_frequent(words, k):
    counts = Counter(words)
    sorted_items = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    result = [item[0] for item in sorted_items[:k]]
    return result
```
