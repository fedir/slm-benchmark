# nemotron-3-nano-4b / py-topk / seed 45 / resample (no feedback)

## Prompt

Write a Python function `top_k_frequent(words, k)` returning the k most frequent words as a list, ordered by frequency descending, ties broken alphabetically. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 63 tokens in 10.6s, finish: stop
- verifier: pass

```python
def top_k_frequent(words, k):
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return sorted(freq, key=lambda w: (-freq[w], w))[:k]
```
