# ornith-9b-mtp / py-topk / seed 44 / harness

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

- 61 tokens in 16.1s, finish: stop
- verifier: pass

```python
from collections import Counter

def top_k_frequent(words, k):
    counts = Counter(words)
    # Sort by frequency descending, then alphabetically ascending for ties
    return sorted(counts, key=lambda w: (-counts[w], w))[:k]
```
