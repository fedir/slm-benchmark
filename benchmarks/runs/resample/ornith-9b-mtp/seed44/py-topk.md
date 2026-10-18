# ornith-9b-mtp / py-topk / seed 44 / resample (no feedback)

## Prompt

Write a Python function `top_k_frequent(words, k)` returning the k most frequent words as a list, ordered by frequency descending, ties broken alphabetically. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: AssertionError)

- 60 tokens in 13.0s, finish: stop
- verifier: FAIL: top_k_frequent(['a','b','a','c','b','a'],2) returned ['a', 'a'], expected ['a','b']

```python
from collections import Counter

def top_k_frequent(words, k):
    counts = Counter(words)
    # Sort by frequency descending, then alphabetically ascending for ties
    return sorted(words, key=lambda w: (-counts[w], w))[:k]
```

## Attempt 2: PASS (hidden: tests passed)

- 70 tokens in 14.9s, finish: stop
- verifier: pass

```python
from collections import Counter

def top_k_frequent(words, k):
    counts = Counter(words)
    # Sort by frequency descending, then alphabetically ascending
    return [w for w, _ in sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:k]]
```
