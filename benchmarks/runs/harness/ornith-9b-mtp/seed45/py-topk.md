# ornith-9b-mtp / py-topk / seed 45 / harness

## Prompt

Write a Python function `top_k_frequent(words, k)` returning the k most frequent words as a list, ordered by frequency descending, ties broken alphabetically. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 73 tokens in 16.2s, finish: stop
- verifier: pass

```python
def top_k_frequent(words, k):
    from collections import Counter
    counts = Counter(words)
    # Sort by frequency descending, then alphabetically ascending for ties
    return [w for w, _ in sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:k]]
```
