# gemma-4-e4b-concise / sql-dept-stats / seed 42 / harness

## Prompt

Table `employees(id INTEGER PRIMARY KEY, name TEXT, dept TEXT, salary INTEGER, manager_id INTEGER)`. Write one SQLite query that returns, for every department, the department name, the number of employees and the total salary, ordered by department name. Reply with ONLY the SQL query in a code block.

## Attempt 1: PASS (hidden: rows match)

- 29 tokens in 8.2s, finish: stop
- verifier: pass

```sqlite
SELECT dept, COUNT(id), SUM(salary)
FROM employees
GROUP BY dept
ORDER BY dept;
```
