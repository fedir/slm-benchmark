# gemma-4-e4b-terse / sh-csv-sum / seed 45 / harness

## Prompt

The file `sales.csv` is comma-separated with a header line. Print the sum of the third column over all data rows, and nothing else. Reply with ONLY the bash command (a one-liner or pipeline) in a code block.

## Attempt 1: PASS (hidden: output matches)

- 28 tokens in 7.6s, finish: stop
- verifier: pass

```bash
awk -F',' 'NR>1 {sum+=$3} END {print sum}' sales.csv
```
