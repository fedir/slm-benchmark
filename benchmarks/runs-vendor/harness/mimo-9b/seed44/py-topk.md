# mimo-9b / py-topk / seed 44 / harness

## Prompt

Write a Python function `top_k_frequent(words, k)` returning the k most frequent words as a list, ordered by frequency descending, ties broken alphabetically. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: NameError: name 'Counter' is not defined (no code fence))

- 37 tokens in 15.1s, finish: stop
- verifier: FAIL: top_k_frequent(['a','b','a','c','b','a'],2) raised NameError: name 'Counter' is not defined; top_k_frequent(['x','y','z'],2) raised NameError: name 'Counter' is not defined; top_k_frequent(['dog','cat','cat','dog'],1) raised NameError: name 'Counter' is not defined

def top_k_frequent(words, k):
    counts = Counter(words)
    return sorted(counts, key=lambda w: (-counts[w], w))[:k]

## Attempt 2: PASS (hidden: tests passed (no code fence))

- 42 tokens in 22.8s, finish: stop
- verifier: pass

from collections import Counter

def top_k_frequent(words, k):
    counts = Counter(words)
    return sorted(counts, key=lambda w: (-counts[w], w))[:k]
