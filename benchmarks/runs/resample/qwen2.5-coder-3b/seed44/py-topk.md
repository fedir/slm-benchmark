# qwen2.5-coder-3b / py-topk / seed 44 / resample (no feedback)

## Prompt

Write a Python function `top_k_frequent(words, k)` returning the k most frequent words as a list, ordered by frequency descending, ties broken alphabetically. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 98 tokens in 9.9s, finish: stop
- verifier: pass

```python
from collections import Counter

def top_k_frequent(words, k):
    # Count the frequency of each word
    word_count = Counter(words)
    # Sort the words by frequency and then alphabetically
    sorted_words = sorted(word_count.items(), key=lambda item: (-item[1], item[0]))
    # Extract the top k words
    top_k = [word for word, _ in sorted_words[:k]]
    return top_k
```
