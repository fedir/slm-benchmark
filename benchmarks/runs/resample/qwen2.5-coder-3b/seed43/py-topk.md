# qwen2.5-coder-3b / py-topk / seed 43 / resample (no feedback)

## Prompt

Write a Python function `top_k_frequent(words, k)` returning the k most frequent words as a list, ordered by frequency descending, ties broken alphabetically. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: AssertionError)

- 83 tokens in 8.6s, finish: stop
- verifier: FAIL: top_k_frequent(['dog','cat','cat','dog'],1) returned ['dog'], expected ['cat']

```python
from collections import Counter

def top_k_frequent(words, k):
    # Count the frequency of each word
    word_counts = Counter(words)
    # Get the k most common words
    most_common = word_counts.most_common(k)
    # Extract the words from the most_common list
    result = [word for word, count in most_common]
    return result
```

## Attempt 2: PASS (hidden: tests passed)

- 109 tokens in 11.2s, finish: stop
- verifier: pass

```python
from collections import Counter
from typing import List

def top_k_frequent(words: List[str], k: int) -> List[str]:
    # Count the frequency of each word
    word_counts = Counter(words)
    # Sort the words by frequency (descending) and alphabetically (ascending)
    sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
    # Extract the top k words
    return [word for word, _ in sorted_words[:k]]
```
