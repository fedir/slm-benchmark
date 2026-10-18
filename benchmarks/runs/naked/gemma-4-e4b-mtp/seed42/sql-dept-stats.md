# gemma-4-e4b-mtp / sql-dept-stats / seed 42 / naked

## Prompt

Table `employees(id INTEGER PRIMARY KEY, name TEXT, dept TEXT, salary INTEGER, manager_id INTEGER)`. Write one SQLite query that returns, for every department, the department name, the number of employees and the total salary, ordered by department name. Reply with ONLY the SQL query in a code block.

## Attempt 1: PASS (hidden: rows match)

- 39 tokens in 7.5s, finish: stop

```sqlite
SELECT
  dept,
  COUNT(id),
  SUM(salary)
FROM employees
GROUP BY
  dept
ORDER BY
  dept;
```
