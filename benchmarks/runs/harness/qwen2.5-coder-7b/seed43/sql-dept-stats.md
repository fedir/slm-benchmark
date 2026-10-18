# qwen2.5-coder-7b / sql-dept-stats / seed 43 / harness

## Prompt

Table `employees(id INTEGER PRIMARY KEY, name TEXT, dept TEXT, salary INTEGER, manager_id INTEGER)`. Write one SQLite query that returns, for every department, the department name, the number of employees and the total salary, ordered by department name. Reply with ONLY the SQL query in a code block.

## Attempt 1: PASS (hidden: rows match)

- 35 tokens in 10.2s, finish: stop
- verifier: pass

```sql
SELECT dept, COUNT(id) AS num_employees, SUM(salary) AS total_salary
FROM employees
GROUP BY dept
ORDER BY dept;
```
