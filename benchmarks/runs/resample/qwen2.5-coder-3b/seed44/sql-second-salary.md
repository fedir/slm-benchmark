# qwen2.5-coder-3b / sql-second-salary / seed 44 / resample (no feedback)

## Prompt

Table `employees(id INTEGER PRIMARY KEY, name TEXT, dept TEXT, salary INTEGER, manager_id INTEGER)`. Write one SQLite query that returns the second highest DISTINCT salary as a single value. Reply with ONLY the SQL query in a code block.

## Attempt 1: PASS (hidden: rows match)

- 24 tokens in 3.7s, finish: stop
- verifier: pass

```sql
SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1;
```
