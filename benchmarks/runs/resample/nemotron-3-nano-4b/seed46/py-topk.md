# nemotron-3-nano-4b / py-topk / seed 46 / resample (no feedback)

## Prompt

Write a Python function `top_k_frequent(words, k)` returning the k most frequent words as a list, ordered by frequency descending, ties broken alphabetically. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 54 tokens in 9.4s, finish: stop
- verifier: pass

```python
from collections import Counter

def top_k_frequent(words, k):
    freq = Counter(words)
    sorted_words = sorted(freq.keys(), key=lambda w: (-freq[w], w))
    return sorted_words[:k]
```
