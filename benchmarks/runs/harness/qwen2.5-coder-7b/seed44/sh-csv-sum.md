# qwen2.5-coder-7b / sh-csv-sum / seed 44 / harness

## Prompt

The file `sales.csv` is comma-separated with a header line. Print the sum of the third column over all data rows, and nothing else. Reply with ONLY the bash command (a one-liner or pipeline) in a code block.

## Attempt 1: PASS (hidden: output matches)

- 27 tokens in 8.6s, finish: stop
- verifier: pass

```bash
awk -F, 'NR>1{sum+=$3} END{print sum}' sales.csv
```
