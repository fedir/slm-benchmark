# nemotron-3-nano-4b / sql-second-salary / seed 46 / resample (no feedback)

## Prompt

Table `employees(id INTEGER PRIMARY KEY, name TEXT, dept TEXT, salary INTEGER, manager_id INTEGER)`. Write one SQLite query that returns the second highest DISTINCT salary as a single value. Reply with ONLY the SQL query in a code block.

## Attempt 1: PASS (hidden: rows match)

- 38 tokens in 7.2s, finish: stop
- verifier: pass

```sql
SELECT COALESCE((SELECT DISTINCT salary FROM employees ORDER BY salary DESC LIMIT 1 OFFSET 1), NULL) AS second_highest_salary;
```
