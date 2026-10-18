# nemotron-3-nano-4b / py-topk / seed 44 / harness

## Prompt

Write a Python function `top_k_frequent(words, k)` returning the k most frequent words as a list, ordered by frequency descending, ties broken alphabetically. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: AssertionError)

- 49 tokens in 9.4s, finish: stop
- verifier: FAIL: top_k_frequent(['a','b','a','c','b','a'],2) returned [('a', 3), ('b', 2)], expected ['a','b']; top_k_frequent(['x','y','z'],2) returned [('x', 1), ('y', 1)], expected ['x','y']; top_k_frequent(['dog','cat','cat','dog'],1) returned [('cat', 2)], expected ['cat']

```python
from collections import Counter

def top_k_frequent(words, k):
    freq = Counter(words)
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:k]
```

## Attempt 2: PASS (hidden: tests passed)

- 54 tokens in 14.8s, finish: stop
- verifier: pass

```python
from collections import Counter

def top_k_frequent(words, k):
    freq = Counter(words)
    sorted_words = sorted(freq.keys(), key=lambda w: (-freq[w], w))
    return sorted_words[:k]
```
