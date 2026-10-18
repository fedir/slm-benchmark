# ornith-9b-mtp / py-topk

- category: python
- result: **FAIL** (AssertionError)
- tokens: 49 in 13s (3.8 t/s), finish: stop

## Prompt

Write a Python function `top_k_frequent(words, k)` returning the k most frequent words as a list, ordered by frequency descending, ties broken alphabetically. Reply with ONLY the code in one code block.

## Answer

```python
from collections import Counter

def top_k_frequent(words, k):
    counts = Counter(word for word in words if word)
    return [word for word, _ in counts.most_common(k)]
```
