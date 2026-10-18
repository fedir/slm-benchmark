# gemma-4-e4b / sh-csv-sum / seed 42 / naked

## Prompt

The file `sales.csv` is comma-separated with a header line. Print the sum of the third column over all data rows, and nothing else. Reply with ONLY the bash command (a one-liner or pipeline) in a code block.

## Attempt 1: PASS (hidden: output matches)

- 36 tokens in 7.2s, finish: stop

```bash
tail -n +2 sales.csv | cut -d',' -f3 | awk '{ sum += $1 } END { print sum }'
```
