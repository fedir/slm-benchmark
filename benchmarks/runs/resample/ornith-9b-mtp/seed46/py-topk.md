# ornith-9b-mtp / py-topk / seed 46 / resample (no feedback)

## Prompt

Write a Python function `top_k_frequent(words, k)` returning the k most frequent words as a list, ordered by frequency descending, ties broken alphabetically. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 58 tokens in 12.8s, finish: stop
- verifier: pass

```python
from collections import Counter

def top_k_frequent(words, k):
    counts = Counter(words)
    return [word for word, _ in sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:k]]
```
