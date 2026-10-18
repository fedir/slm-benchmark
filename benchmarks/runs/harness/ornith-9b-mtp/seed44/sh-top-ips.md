# ornith-9b-mtp / sh-top-ips / seed 44 / harness

## Prompt

The file `access.log` has an IP address as the first space-separated field of each line. Print the 3 most frequent IP addresses with their counts, one per line as `COUNT IP`, most frequent first, ties broken by IP address in ascending string order. Reply with ONLY the bash command (a one-liner or pipeline) in a code block.

## Attempt 1: PASS (hidden: output matches)

- 47 tokens in 13.2s, finish: stop
- verifier: pass

```bash
awk '{c[$1]++} END {for (i in c) print c[i], i}' access.log | sort -k1,1nr -k2,2 | head -3
```
