# qwen2.5-coder-3b / py-topk / seed 46 / resample (no feedback)

## Prompt

Write a Python function `top_k_frequent(words, k)` returning the k most frequent words as a list, ordered by frequency descending, ties broken alphabetically. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: AssertionError)

- 90 tokens in 9.3s, finish: stop
- verifier: FAIL: top_k_frequent(['dog','cat','cat','dog'],1) returned ['dog'], expected ['cat']

```python
from collections import Counter

def top_k_frequent(words, k):
    # Count the frequency of each word in the list
    word_counts = Counter(words)
    # Get the k most common words, ordered by frequency descending and alphabetically
    top_k = word_counts.most_common(k)
    # Extract the words from the top_k tuple pairs
    return [word for word, count in top_k]
```

## Attempt 2: PASS (hidden: tests passed)

- 101 tokens in 10.2s, finish: stop
- verifier: pass

```python
from collections import Counter

def top_k_frequent(words, k):
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Sort words by frequency and then alphabetically
    sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
    
    # Extract the top k frequent words
    top_k = [word for word, _ in sorted_words[:k]]
    
    return top_k
```
