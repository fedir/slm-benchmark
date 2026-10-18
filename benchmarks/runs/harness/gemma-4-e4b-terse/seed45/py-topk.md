# gemma-4-e4b-terse / py-topk / seed 45 / harness

## Prompt

Write a Python function `top_k_frequent(words, k)` returning the k most frequent words as a list, ordered by frequency descending, ties broken alphabetically. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 85 tokens in 15.7s, finish: stop
- verifier: pass

```python
import heapq
from collections import Counter

def top_k_frequent(words, k):
    counts = Counter(words)
    heap = []
    for word, freq in counts.items():
        heapq.heappush(heap, (-freq, word))
    return [word for _, word in heapq.nsmallest(k, heap)]
```
