# ornith-9b-mtp / py-topk / seed 42 / harness

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

- 53 tokens in 16.9s, finish: stop
- verifier: pass

```python
from collections import Counter

def top_k_frequent(words, k):
    counts = Counter(word for word in words if word)
    return sorted(counts, key=lambda word: (-counts[word], word))[:k]
```
