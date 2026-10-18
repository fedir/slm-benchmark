# nemotron-3-nano-4b / sql-dept-stats / seed 44 / resample (no feedback)

## Prompt

Table `employees(id INTEGER PRIMARY KEY, name TEXT, dept TEXT, salary INTEGER, manager_id INTEGER)`. Write one SQLite query that returns, for every department, the department name, the number of employees and the total salary, ordered by department name. Reply with ONLY the SQL query in a code block.

## Attempt 1: PASS (hidden: rows match)

- 47 tokens in 9.1s, finish: stop
- verifier: pass

```sql
SELECT 
    dept AS department_name,
    COUNT(*) AS number_of_employees,
    SUM(salary) AS total_salary
FROM employees
GROUP BY dept
ORDER BY department_name;
```
