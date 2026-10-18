# mimo-9b / py-topk

- category: python
- result: **PASS** (tests passed (no code fence))
- tokens: 76 in 24s (3.1 t/s), finish: stop

## Prompt

Write a Python function `top_k_frequent(words, k)` returning the k most frequent words as a list, ordered by frequency descending, ties broken alphabetically. Reply with ONLY the code in one code block.

## Answer

def top_k_frequent(words, k):
    from collections import Counter

    counts = Counter(words)

    # Sort by (-count, word): frequency descending, ties alphabetically.
    result = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

    return [word for word, _ in result[:k]]
