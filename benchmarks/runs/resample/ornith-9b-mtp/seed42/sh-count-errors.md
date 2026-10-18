# ornith-9b-mtp / sh-count-errors / seed 42 / resample (no feedback)

## Prompt

The file `app.log` is in the current directory. Print the number of lines that contain the exact word ERROR (uppercase), and nothing else. Reply with ONLY the bash command (a one-liner or pipeline) in a code block.

## Attempt 1: FAIL (hidden: output ['0'], expected ['3'])

- 116 tokens in 25.2s, finish: stop
- verifier: FAIL: on a small example the command's output ['0'], expected ['4']

```bash
grep -c '^ERROR$' app.log
```

This counts lines that contain **only** the exact word `ERROR` — meaning the entire line is exactly `ERROR` with no other characters.

If you instead want lines where `ERROR` appears as a standalone word but other content may also be present (e.g. `ERROR: something`), use:

```bash
grep -cw 'ERROR' app.log
```

The `-w` flag matches `ERROR` as a whole word, allowing surrounding characters like punctuation or spaces.

## Attempt 2: FAIL (hidden: output ['0'], expected ['3'])

- 15 tokens in 6.4s, finish: stop
- verifier: FAIL: on a small example the command's output ['0'], expected ['4']

```bash
grep -c '^ERROR$' app.log
```

## Attempt 3: FAIL (hidden: output ['0'], expected ['3'])

- 15 tokens in 6.4s, finish: stop
- verifier: FAIL: on a small example the command's output ['0'], expected ['4']

```bash
grep -c '^ERROR$' app.log
```
