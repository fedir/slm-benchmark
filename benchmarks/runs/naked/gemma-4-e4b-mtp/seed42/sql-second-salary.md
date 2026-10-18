# gemma-4-e4b-mtp / sql-second-salary / seed 42 / naked

## Prompt

Table `employees(id INTEGER PRIMARY KEY, name TEXT, dept TEXT, salary INTEGER, manager_id INTEGER)`. Write one SQLite query that returns the second highest DISTINCT salary as a single value. Reply with ONLY the SQL query in a code block.

## Attempt 1: FAIL (hidden: returned [(90000,)] (1 rows), expected [(70000,)] (1 rows))

- 21 tokens in 5.6s, finish: stop

```sqlite
SELECT salary FROM employees ORDER BY salary DESC LIMIT 1 OFFSET 1;
```
