# nemotron-3-nano-4b / py-topk / seed 42 / resample (no feedback)

## Prompt

Write a Python function `top_k_frequent(words, k)` returning the k most frequent words as a list, ordered by frequency descending, ties broken alphabetically. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 47 tokens in 8.5s, finish: stop
- verifier: pass

```python
from collections import Counter

def top_k_frequent(words, k):
    freq = Counter(words)
    return sorted(freq.keys(), key=lambda x: (-freq[x], x))[:k]
```
