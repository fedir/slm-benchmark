# nemotron-3-nano-4b / py-topk / seed 43 / harness

## Prompt

Write a Python function `top_k_frequent(words, k)` returning the k most frequent words as a list, ordered by frequency descending, ties broken alphabetically. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 48 tokens in 8.9s, finish: stop
- verifier: pass

```python
from collections import Counter

def top_k_frequent(words, k):
    freq = Counter(words)
    return sorted(freq.keys(), key=lambda w: (-freq[w], w))[:k]
```
