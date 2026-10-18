# ornith-9b-mtp / py-topk / seed 42 / resample (no feedback)

## Prompt

Write a Python function `top_k_frequent(words, k)` returning the k most frequent words as a list, ordered by frequency descending, ties broken alphabetically. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: AssertionError)

- 49 tokens in 12.4s, finish: stop
- verifier: FAIL: top_k_frequent(['dog','cat','cat','dog'],1) returned ['dog'], expected ['cat']

```python
from collections import Counter

def top_k_frequent(words, k):
    counts = Counter(word for word in words if word)
    return [word for word, _ in counts.most_common(k)]
```

## Attempt 2: PASS (hidden: tests passed)

- 70 tokens in 14.5s, finish: stop
- verifier: pass

```python
from collections import Counter

def top_k_frequent(words, k):
    counts = Counter(words)
    # Sort by frequency descending, then alphabetically ascending
    return [word for word, _ in sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:k]]
```
