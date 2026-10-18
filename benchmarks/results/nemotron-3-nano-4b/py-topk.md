# nemotron-3-nano-4b / py-topk

- category: python
- result: **PASS** (tests passed)
- tokens: 47 in 9s (5.3 t/s), finish: stop

## Prompt

Write a Python function `top_k_frequent(words, k)` returning the k most frequent words as a list, ordered by frequency descending, ties broken alphabetically. Reply with ONLY the code in one code block.

## Answer

```python
from collections import Counter

def top_k_frequent(words, k):
    freq = Counter(words)
    return sorted(freq.keys(), key=lambda x: (-freq[x], x))[:k]
```
