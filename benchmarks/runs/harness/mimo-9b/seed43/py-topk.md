# mimo-9b / py-topk / seed 43 / harness

## Prompt

Write a Python function `top_k_frequent(words, k)` returning the k most frequent words as a list, ordered by frequency descending, ties broken alphabetically. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: NameError: name 'collections' is not defined. Did you forget to import 'collections'? (no code fence))

- 34 tokens in 11.4s, finish: stop
- verifier: FAIL: top_k_frequent(['a','b','a','c','b','a'],2) raised NameError: name 'collections' is not defined; top_k_frequent(['x','y','z'],2) raised NameError: name 'collections' is not defined; top_k_frequent(['dog','cat','cat','dog'],1) raised NameError: name 'collections' is not defined

def top_k_frequent(words, k):
    freq = collections.Counter(words)
    return [w for w, _ in freq.most_common(k)]

## Attempt 2: FAIL (hidden: AssertionError (no code fence))

- 37 tokens in 17.8s, finish: stop
- verifier: FAIL: top_k_frequent(['dog','cat','cat','dog'],1) returned ['dog'], expected ['cat']

import collections

def top_k_frequent(words, k):
    freq = collections.Counter(words)
    return [w for w, _ in freq.most_common(k)]

## Attempt 3: PASS (hidden: tests passed (no code fence))

- 51 tokens in 25.5s, finish: stop
- verifier: pass

import collections

def top_k_frequent(words, k):
    freq = collections.Counter(words)
    return [w for w, _ in sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:k]]
