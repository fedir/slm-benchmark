# qwen2.5-coder-3b / py-topk

- category: python
- result: **PASS** (tests passed)
- tokens: 89 in 9s (10.0 t/s), finish: stop

## Prompt

Write a Python function `top_k_frequent(words, k)` returning the k most frequent words as a list, ordered by frequency descending, ties broken alphabetically. Reply with ONLY the code in one code block.

## Answer

```python
from collections import Counter

def top_k_frequent(words, k):
    # Count the frequency of each word
    frequency = Counter(words)
    # Sort words by frequency and then alphabetically
    sorted_words = sorted(frequency.items(), key=lambda item: (-item[1], item[0]))
    # Return the top k words
    return [word for word, freq in sorted_words[:k]]
```
