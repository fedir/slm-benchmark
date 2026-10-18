# qwen2.5-coder-3b / sql-dept-stats / seed 42 / resample (no feedback)

## Prompt

Table `employees(id INTEGER PRIMARY KEY, name TEXT, dept TEXT, salary INTEGER, manager_id INTEGER)`. Write one SQLite query that returns, for every department, the department name, the number of employees and the total salary, ordered by department name. Reply with ONLY the SQL query in a code block.

## Attempt 1: PASS (hidden: rows match)

- 34 tokens in 4.8s, finish: stop
- verifier: pass

```sql
SELECT dept, COUNT(*) AS num_employees, SUM(salary) AS total_salary
FROM employees
GROUP BY dept
ORDER BY dept;
```
