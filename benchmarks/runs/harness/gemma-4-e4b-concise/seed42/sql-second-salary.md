# gemma-4-e4b-concise / sql-second-salary / seed 42 / harness

## Prompt

Table `employees(id INTEGER PRIMARY KEY, name TEXT, dept TEXT, salary INTEGER, manager_id INTEGER)`. Write one SQLite query that returns the second highest DISTINCT salary as a single value. Reply with ONLY the SQL query in a code block.

## Attempt 1: FAIL (hidden: returned [(90000,)] (1 rows), expected [(70000,)] (1 rows))

- 20 tokens in 6.0s, finish: stop
- verifier: FAIL: on a small example table the query returned [(300,)] (1 rows), expected [(200,)] (1 rows)

```sqlite
SELECT salary FROM employees ORDER BY salary DESC LIMIT 1 OFFSET 1
```

## Attempt 2: PASS (hidden: rows match)

- 21 tokens in 8.6s, finish: stop
- verifier: pass

```sqlite
SELECT DISTINCT salary FROM employees ORDER BY salary DESC LIMIT 1 OFFSET 1
```
