# qwen2.5-coder-3b / py-topk / seed 42 / harness

## Prompt

Write a Python function `top_k_frequent(words, k)` returning the k most frequent words as a list, ordered by frequency descending, ties broken alphabetically. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 151 tokens in 14.7s, finish: stop
- verifier: pass

```python
from collections import Counter

def top_k_frequent(words, k):
    # Count the frequency of each word
    frequency = Counter(words)
    
    # Sort words by frequency (descending) and then alphabetically
    sorted_words = sorted(frequency.items(), key=lambda item: (-item[1], item[0]))
    
    # Extract the top k frequent words
    top_k = [word for word, _ in sorted_words[:k]]
    
    return top_k

# Example usage:
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
k = 2
print(top_k_frequent(words, k))  # Output: ['apple', 'banana']
```
