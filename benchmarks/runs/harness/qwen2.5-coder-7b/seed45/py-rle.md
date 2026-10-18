# qwen2.5-coder-7b / py-rle / seed 45 / harness

## Prompt

Write a Python function `rle_encode(s)` that run-length encodes a string: each run of identical characters becomes the character followed by the run length, e.g. 'aaabcc' becomes 'a3b1c2'. The empty string gives ''. Reply with ONLY the code in one code block.

## Attempt 1: PASS (hidden: tests passed)

- 43 tokens in 11.8s, finish: stop
- verifier: pass

```python
from itertools import groupby

def rle_encode(s):
    return ''.join(f'{char}{sum(1 for _ in group)}' for char, group in groupby(s))
```
