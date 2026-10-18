# gemma-4-e4b-terse / sh-csv-sum / seed 44 / harness

## Prompt

The file `sales.csv` is comma-separated with a header line. Print the sum of the third column over all data rows, and nothing else. Reply with ONLY the bash command (a one-liner or pipeline) in a code block.

## Attempt 1: PASS (hidden: output matches)

- 35 tokens in 8.5s, finish: stop
- verifier: pass

```bash
tail -n +2 sales.csv | cut -d',' -f3 | awk '{s+=$1} END {print s}'
```
