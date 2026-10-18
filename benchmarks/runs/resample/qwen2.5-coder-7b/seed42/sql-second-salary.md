# qwen2.5-coder-7b / sql-second-salary / seed 42 / resample (no feedback)

## Prompt

Table `employees(id INTEGER PRIMARY KEY, name TEXT, dept TEXT, salary INTEGER, manager_id INTEGER)`. Write one SQLite query that returns the second highest DISTINCT salary as a single value. Reply with ONLY the SQL query in a code block.

## Attempt 1: PASS (hidden: rows match)

- 24 tokens in 8.0s, finish: stop
- verifier: pass

```sql
SELECT MAX(salary) FROM employees WHERE salary < (SELECT MAX(salary) FROM employees);
```
