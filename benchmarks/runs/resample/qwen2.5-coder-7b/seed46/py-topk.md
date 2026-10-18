# qwen2.5-coder-7b / py-topk / seed 46 / resample (no feedback)

## Prompt

Write a Python function `top_k_frequent(words, k)` returning the k most frequent words as a list, ordered by frequency descending, ties broken alphabetically. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: AssertionError)

- 35 tokens in 10.0s, finish: stop
- verifier: FAIL: top_k_frequent(['dog','cat','cat','dog'],1) returned ['dog'], expected ['cat']

```python
from collections import Counter

def top_k_frequent(words, k):
    return [word for word, _ in Counter(words).most_common(k)]
```

## Attempt 2: PASS (hidden: tests passed)

- 49 tokens in 17.5s, finish: stop
- verifier: pass

```python
from collections import Counter
import heapq

def top_k_frequent(words, k):
    count = Counter(words)
    return heapq.nsmallest(k, count.keys(), key=lambda word: (-count[word], word))
```
