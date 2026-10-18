# nemotron-3-nano-4b / sh-csv-sum / seed 43 / harness

## Prompt

The file `sales.csv` is comma-separated with a header line. Print the sum of the third column over all data rows, and nothing else. Reply with ONLY the bash command (a one-liner or pipeline) in a code block.

## Attempt 1: PASS (hidden: output matches)

- 28 tokens in 6.6s, finish: stop
- verifier: pass

```bash
tail -n +2 sales.csv | awk -F, '{sum+=$3} END {print sum}'
```
