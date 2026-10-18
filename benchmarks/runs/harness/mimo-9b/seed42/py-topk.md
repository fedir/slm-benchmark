# mimo-9b / py-topk / seed 42 / harness

## Prompt

Write a Python function `top_k_frequent(words, k)` returning the k most frequent words as a list, ordered by frequency descending, ties broken alphabetically. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed (no code fence))

- 76 tokens in 22.7s, finish: stop
- verifier: pass

def top_k_frequent(words, k):
    from collections import Counter

    counts = Counter(words)

    # Sort by (-count, word): frequency descending, ties alphabetically.
    result = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

    return [word for word, _ in result[:k]]
