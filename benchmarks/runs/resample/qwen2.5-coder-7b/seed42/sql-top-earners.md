# qwen2.5-coder-7b / sql-top-earners / seed 42 / resample (no feedback)

## Prompt

Table `employees(id INTEGER PRIMARY KEY, name TEXT, dept TEXT, salary INTEGER, manager_id INTEGER)`. Write one SQLite query that returns the names of employees who earn more than 60000, highest salary first, ties broken by name alphabetically. Reply with ONLY the SQL query in a code block.

## Attempt 1: PASS (hidden: rows match)

- 26 tokens in 8.4s, finish: stop
- verifier: pass

```sql
SELECT name FROM employees WHERE salary > 60000 ORDER BY salary DESC, name ASC;
```
