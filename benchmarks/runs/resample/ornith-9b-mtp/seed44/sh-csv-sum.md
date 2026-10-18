# ornith-9b-mtp / sh-csv-sum / seed 44 / resample (no feedback)

## Prompt

The file `sales.csv` is comma-separated with a header line. Print the sum of the third column over all data rows, and nothing else. Reply with ONLY the bash command (a one-liner or pipeline) in a code block.

## Attempt 1: PASS (hidden: output matches)

- 26 tokens in 8.4s, finish: stop
- verifier: pass

```bash
awk -F, 'NR>1{s+=$3} END{print s}' sales.csv
```
