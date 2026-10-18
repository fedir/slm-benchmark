# qwen2.5-coder-7b / sql-second-salary / seed 43 / harness

## Prompt

Table `employees(id INTEGER PRIMARY KEY, name TEXT, dept TEXT, salary INTEGER, manager_id INTEGER)`. Write one SQLite query that returns the second highest DISTINCT salary as a single value. Reply with ONLY the SQL query in a code block.

## Attempt 1: PASS (hidden: rows match)

- 21 tokens in 7.5s, finish: stop
- verifier: pass

```sql
SELECT DISTINCT salary FROM employees ORDER BY salary DESC LIMIT 1, 1;
```
