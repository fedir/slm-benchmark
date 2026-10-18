# qwen2.5-coder-3b / sql-second-salary / seed 46 / harness

## Prompt

Table `employees(id INTEGER PRIMARY KEY, name TEXT, dept TEXT, salary INTEGER, manager_id INTEGER)`. Write one SQLite query that returns the second highest DISTINCT salary as a single value. Reply with ONLY the SQL query in a code block.

## Attempt 1: FAIL (hidden: returned [(90000,)] (1 rows), expected [(70000,)] (1 rows))

- 22 tokens in 3.5s, finish: stop
- verifier: FAIL: on a small example table the query returned [(300,)] (1 rows), expected [(200,)] (1 rows)

```sql
SELECT salary FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1;
```

## Attempt 2: PASS (hidden: rows match)

- 31 tokens in 4.9s, finish: stop
- verifier: pass

```sql
SELECT MAX(salary) AS second_highest_salary
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);
```
