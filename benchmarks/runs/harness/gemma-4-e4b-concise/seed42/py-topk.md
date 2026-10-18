# gemma-4-e4b-concise / py-topk / seed 42 / harness

## Prompt

Write a Python function `top_k_frequent(words, k)` returning the k most frequent words as a list, ordered by frequency descending, ties broken alphabetically. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 78 tokens in 14.5s, finish: stop
- verifier: pass

```python
from collections import Counter

def top_k_frequent(words, k):
    word_counts = Counter(words)
    sorted_items = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))
    return [item[0] for item in sorted_items[:k]]
```
