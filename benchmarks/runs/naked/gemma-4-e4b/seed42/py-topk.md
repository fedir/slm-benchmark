# gemma-4-e4b / py-topk / seed 42 / naked

## Prompt

Write a Python function `top_k_frequent(words, k)` returning the k most frequent words as a list, ordered by frequency descending, ties broken alphabetically. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 241 tokens in 36.7s, finish: stop

```python
from collections import Counter

def top_k_frequent(words, k):
    """
    Returns the k most frequent words as a list, ordered by frequency descending, ties broken alphabetically.

    Args:
        words: A list of strings.
        k: An integer representing the number of top frequent words to return.

    Returns:
        A list of the k most frequent words.
    """
    # Count the frequency of each word
    word_counts = Counter(words)

    # Get items (word, count) and sort them
    # The sorting criteria are:
    # 1. Frequency (descending) -> use -count
    # 2. Word (alphabetical ascending) -> use word itself
    sorted_items = sorted(
        word_counts.items(),
        key=lambda item: (-item[1], item[0])
    )

    # Extract the words from the top k items
    top_k_words = [item[0] for item in sorted_items[:k]]

    return top_k_words
```
