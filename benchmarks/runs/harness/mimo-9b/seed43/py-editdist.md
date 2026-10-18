# mimo-9b / py-editdist / seed 43 / harness

## Prompt

Write a Python function `edit_distance(a, b)` returning the Levenshtein edit distance between two strings (insert, delete, replace, each cost 1). It is tested on strings of 1500 characters. Reply with ONLY the code in one code block.

## Attempt 1: FAIL (hidden: AssertionError)

- 190 tokens in 50.7s, finish: stop
- verifier: FAIL: edit_distance('horse','ros') returned 6, expected 3; edit_distance('a','a') returned 1, expected 0; edit_distance('abc','xyz') returned 6, expected 3

```python
def edit_distance(a, b):
    if len(a) < len(b):
        a, b = b, a

    previous_row = list(range(len(b) + 1))
    current_row = [0] * (len(b) + 1)

    for i in range(1, len(a) + 1):
        current_row[0] = i
        for j in range(1, len(b) + 1):
            cost = 1 + min(
                previous_row[j],
                current_row[j - 1],
                previous_row[j - 1] + (0 if a[i - 1] == b[j - 1] else 1)
            )
            current_row[j] = cost
        previous_row, current_row = current_row, previous_row

    return previous_row[-1]
```

## Attempt 2: FAIL (hidden: AssertionError)

- 191 tokens in 59.6s, finish: stop
- verifier: FAIL: edit_distance('horse','ros') returned 6, expected 3; edit_distance('a','a') returned 1, expected 0; edit_distance('abc','xyz') returned 6, expected 3

```python
def edit_distance(a, b):
    if len(a) < len(b):
        a, b = b, a

    previous_row = list(range(len(b) + 1))
    current_row = [0] * (len(b) + 1)

    for i in range(1, len(a) + 1):
        current_row[0] = i
        for j in range(1, len(b) + 1):
            substitution_cost = 0 if a[i - 1] == b[j - 1] else 1
            current_row[j] = 1 + min(
                previous_row[j],
                current_row[j - 1],
                previous_row[j - 1] + substitution_cost
            )
        previous_row, current_row = current_row, previous_row

    return previous_row[-1]
```

## Attempt 3: FAIL (hidden: AssertionError)

- 191 tokens in 71.2s, finish: stop
- verifier: FAIL: edit_distance('horse','ros') returned 6, expected 3; edit_distance('a','a') returned 1, expected 0; edit_distance('abc','xyz') returned 6, expected 3

```python
def edit_distance(a, b):
    if len(a) < len(b):
        a, b = b, a

    previous_row = list(range(len(b) + 1))
    current_row = [0] * (len(b) + 1)

    for i in range(1, len(a) + 1):
        current_row[0] = i
        for j in range(1, len(b) + 1):
            substitution_cost = 0 if a[i - 1] == b[j - 1] else 1
            current_row[j] = 1 + min(
                previous_row[j],
                current_row[j - 1],
                previous_row[j - 1] + substitution_cost
            )
        previous_row, current_row = current_row, previous_row

    return previous_row[-1]
```
