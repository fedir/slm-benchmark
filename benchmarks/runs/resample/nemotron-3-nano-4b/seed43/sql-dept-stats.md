# nemotron-3-nano-4b / sql-dept-stats / seed 43 / resample (no feedback)

## Prompt

Table `employees(id INTEGER PRIMARY KEY, name TEXT, dept TEXT, salary INTEGER, manager_id INTEGER)`. Write one SQLite query that returns, for every department, the department name, the number of employees and the total salary, ordered by department name. Reply with ONLY the SQL query in a code block.

## Attempt 1: PASS (hidden: rows match)

- 37 tokens in 7.7s, finish: stop
- verifier: pass

```sql
SELECT dept, COUNT(*) AS employee_count, SUM(salary) AS total_salary
FROM employees
GROUP BY dept
ORDER BY dept;
```
