# mimo-9b / sh-rename-ext / seed 43 / harness

## Prompt

The current directory contains some `.txt` files and other files. Rename every `.txt` file to the same name with the extension `.md`. Reply with ONLY the bash command (a one-liner or pipeline) in a code block.

## Attempt 1: FAIL (hidden: output ['a.txt.md', 'b.txt.md', 'c.txt.md', 'notes.bak'], expected ['a.md', 'b.md', 'c.md', 'notes.bak'])

- 24 tokens in 9.1s, finish: stop
- verifier: FAIL: on a small example the command's output ['x.txt.md', 'y.txt.md', 'z.doc'], expected ['x.md', 'y.md', 'z.doc']

```bash
find . -type f -name '*.txt' -exec mv {} {}.md \;
```

## Attempt 2: PASS (hidden: output matches)

- 34 tokens in 15.4s, finish: stop
- verifier: pass

```bash
find . -type f -name '*.txt' | while read f; do mv "$f" "${f%.txt}.md"; done
```
