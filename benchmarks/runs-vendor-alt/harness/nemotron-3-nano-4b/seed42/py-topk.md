# nemotron-3-nano-4b / py-topk / seed 42 / harness

## Prompt

Write a Python function `top_k_frequent(words, k)` returning the k most frequent words as a list, ordered by frequency descending, ties broken alphabetically. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 81 tokens in 14.4s, finish: stop
- verifier: pass

```python
def top_k_frequent(words, k):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    return [word for word, _ in sorted_words[:k]]
```
