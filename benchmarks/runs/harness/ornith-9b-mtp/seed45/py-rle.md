# ornith-9b-mtp / py-rle / seed 45 / harness

## Prompt

Write a Python function `rle_encode(s)` that run-length encodes a string: each run of identical characters becomes the character followed by the run length, e.g. 'aaabcc' becomes 'a3b1c2'. The empty string gives ''. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: TypeError: can't multiply sequence by non-int of type 'itertools._grouper')

- 35 tokens in 10.8s, finish: stop
- verifier: FAIL: rle_encode('wwwwb') raised TypeError: can't multiply sequence by non-int of type 'itertools._grouper'; rle_encode('abc') raised TypeError: can't multiply sequence by non-int of type 'itertools._grouper'

```python
def rle_encode(s):
    return ''.join(c * n for c, n in __import__('itertools').groupby(s))
```

## Attempt 2: FAIL (hidden: AssertionError)

- 52 tokens in 17.3s, finish: stop
- verifier: FAIL: rle_encode('wwwwb') returned 'wwwwb', expected 'w4b1'; rle_encode('abc') returned 'abc', expected 'a1b1c1'

```python
def rle_encode(s):
    result = ''
    for c, group in __import__('itertools').groupby(s):
        result += c * sum(1 for _ in group)
    return result
```

## Attempt 3: FAIL (hidden: AssertionError)

- 42 tokens in 21.9s, finish: stop
- verifier: FAIL: rle_encode('wwwwb') returned 'wwwwb', expected 'w4b1'; rle_encode('abc') returned 'abc', expected 'a1b1c1'

```python
def rle_encode(s):
    return ''.join(c * sum(1 for _ in group) for c, group in __import__('itertools').groupby(s))
```
