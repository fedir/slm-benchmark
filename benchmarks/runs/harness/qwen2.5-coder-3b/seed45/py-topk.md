# qwen2.5-coder-3b / py-topk / seed 45 / harness

## Prompt

Write a Python function `top_k_frequent(words, k)` returning the k most frequent words as a list, ordered by frequency descending, ties broken alphabetically. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 166 tokens in 15.8s, finish: stop
- verifier: pass

```python
def top_k_frequent(words, k):
    # Count the frequency of each word
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    # Sort words by frequency and then alphabetically
    sorted_words = sorted(word_count.items(), key=lambda item: (-item[1], item[0]))
    
    # Return the top k words
    return [word for word, _ in sorted_words[:k]]

# Example usage
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
k = 2
print(top_k_frequent(words, k))  # Output: ['apple', 'banana']
```
