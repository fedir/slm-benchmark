# Benchmark summary

Sampling: temp 0.6, top_p 0.95, top_k 20, seed 42, max_tokens 512, thinking requested off. CPU, 4 threads.

| model | kubectl | python | regex | total | avg t/s | avg s/answer | truncated |
|---|---|---|---|---|---|---|---|
| ornith-9b-mtp | 3/4 | 3/4 | 3/3 | 9/11 | 3.2 | 29 | 0 |
| mimo-9b | 3/4 | 3/4 | 3/3 | 9/11 | 2.9 | 21 | 0 |
| nemotron-3-nano-4b | 2/4 | 4/4 | 2/3 | 8/11 | 5.2 | 10 | 0 |
| qwen2.5-coder-3b | 4/4 | 3/4 | 0/3 | 7/11 | 8.3 | 6 | 0 |

## Per question

| question | ornith-9b-mtp | mimo-9b | nemotron-3-nano-4b | qwen2.5-coder-3b | qwen2.5-coder-7b |
|---|---|---|---|---|---|
| regex-ipv4 | PASS | PASS | PASS | FAIL | - |
| regex-date | PASS | PASS | FAIL | FAIL | - |
| regex-hexcolor | PASS | PASS | PASS | FAIL | - |
| py-intervals | PASS | PASS | PASS | PASS | - |
| py-lis | PASS | FAIL | PASS | FAIL | - |
| py-topk | FAIL | PASS | PASS | PASS | - |
| py-coins | PASS | PASS | PASS | PASS | - |
| kubectl-pods-sorted | PASS | FAIL | FAIL | PASS | - |
| kubectl-scale | PASS | PASS | PASS | PASS | - |
| kubectl-logs | FAIL | PASS | FAIL | PASS | - |
| kubectl-nodes-names | PASS | PASS | PASS | PASS | - |
