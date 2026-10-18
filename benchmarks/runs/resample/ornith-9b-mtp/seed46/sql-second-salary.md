# ornith-9b-mtp / sql-second-salary / seed 46 / resample (no feedback)

## Prompt

Table `employees(id INTEGER PRIMARY KEY, name TEXT, dept TEXT, salary INTEGER, manager_id INTEGER)`. Write one SQLite query that returns the second highest DISTINCT salary as a single value. Reply with ONLY the SQL query in a code block.

## Attempt 1: FAIL (hidden: returned [(60000,)] (1 rows), expected [(70000,)] (1 rows))

- 41 tokens in 9.9s, finish: stop
- verifier: FAIL: on a small example table the query returned [(100,)] (1 rows), expected [(200,)] (1 rows)

```sql
SELECT MIN(salary)
FROM (
    SELECT DISTINCT salary
    FROM employees
    ORDER BY salary DESC
    LIMIT 2
    OFFSET 1
);
```

## Attempt 2: PASS (hidden: rows match)

- 22 tokens in 6.7s, finish: stop
- verifier: pass

```sql
SELECT DISTINCT salary FROM employees ORDER BY salary DESC LIMIT 1 OFFSET 1;
```
