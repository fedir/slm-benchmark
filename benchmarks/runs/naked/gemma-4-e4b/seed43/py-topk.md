# gemma-4-e4b / py-topk / seed 43 / naked

## Prompt

Write a Python function `top_k_frequent(words, k)` returning the k most frequent words as a list, ordered by frequency descending, ties broken alphabetically. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 238 tokens in 37.8s, finish: stop

```python
from collections import Counter

def top_k_frequent(words, k):
    """
    Returns the k most frequent words as a list, ordered by frequency descending, ties broken alphabetically.
    """
    # Count the frequency of each word
    word_counts = Counter(words)

    # Convert the Counter items to a list of tuples: (word, frequency)
    items = word_counts.items()

    # Sort the items:
    # The primary sorting key is frequency (descending: -frequency)
    # The secondary sorting key is the word itself (alphabetical: word)
    # Python's sort is stable, but a custom lambda handles both criteria efficiently.
    # We use -frequency because Python's sort is ascending by default.
    sorted_items = sorted(items, key=lambda item: (-item[1], item[0]))

    # Extract the words from the top k items
    top_k_words = [item[0] for item in sorted_items[:k]]

    return top_k_words
```
