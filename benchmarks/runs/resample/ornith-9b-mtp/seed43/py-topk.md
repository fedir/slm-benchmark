# ornith-9b-mtp / py-topk / seed 43 / resample (no feedback)

## Prompt

Write a Python function `top_k_frequent(words, k)` returning the k most frequent words as a list, ordered by frequency descending, ties broken alphabetically. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: AssertionError)

- 66 tokens in 14.1s, finish: stop
- verifier: FAIL: top_k_frequent(['a','b','a','c','b','a'],2) returned ['a', 'a'], expected ['a','b']

```python
from collections import Counter

def top_k_frequent(words, k):
    counts = Counter(words)
    # Sort by frequency descending, then alphabetically for ties
    sorted_words = sorted(words, key=lambda w: (-counts[w], w))
    return sorted_words[:k]
```

## Attempt 2: PASS (hidden: tests passed)

- 58 tokens in 12.6s, finish: stop
- verifier: pass

```python
from collections import Counter


def top_k_frequent(words, k):
    counts = Counter(words)
    return [w for w, _ in sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:k]]
```
