# ornith-9b-mtp / py-topk / seed 44 / naked

## Prompt

Write a Python function `top_k_frequent(words, k)` returning the k most frequent words as a list, ordered by frequency descending, ties broken alphabetically. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: AssertionError)

- 60 tokens in 13.7s, finish: stop

```python
from collections import Counter

def top_k_frequent(words, k):
    counts = Counter(words)
    # Sort by frequency descending, then alphabetically ascending for ties
    return sorted(words, key=lambda w: (-counts[w], w))[:k]
```
