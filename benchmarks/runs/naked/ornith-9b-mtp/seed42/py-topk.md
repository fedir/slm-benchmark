# ornith-9b-mtp / py-topk / seed 42 / naked

## Prompt

Write a Python function `top_k_frequent(words, k)` returning the k most frequent words as a list, ordered by frequency descending, ties broken alphabetically. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: AssertionError)

- 49 tokens in 11.9s, finish: stop

```python
from collections import Counter

def top_k_frequent(words, k):
    counts = Counter(word for word in words if word)
    return [word for word, _ in counts.most_common(k)]
```
