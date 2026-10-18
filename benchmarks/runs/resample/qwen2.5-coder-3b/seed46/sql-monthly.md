# qwen2.5-coder-3b / sql-monthly / seed 46 / resample (no feedback)

## Prompt

Tables `customers(id INTEGER PRIMARY KEY, name TEXT)` and `orders(id INTEGER PRIMARY KEY, customer_id INTEGER, amount INTEGER, placed_on TEXT)` (`placed_on` is 'YYYY-MM-DD'). Write one SQLite query that returns the total order amount per month (as 'YYYY-MM') for orders placed in 2024, only for months that have orders, ordered by month. Reply with ONLY the SQL query in a code block.

## Attempt 1: FAIL (hidden: the query fails: OperationalError: no such function: DATE_TRUNC)

- 66 tokens in 7.3s, finish: stop
- verifier: FAIL: on a small example table the query the query fails: OperationalError: no such function: DATE_TRUNC

```sql
SELECT DATE_TRUNC('month', placed_on) AS month, SUM(amount) AS total_amount
FROM orders
WHERE STRFTIME('%Y', placed_on) = '2024'
GROUP BY DATE_TRUNC('month', placed_on)
HAVING COUNT(*) > 0
ORDER BY month;
```

## Attempt 2: PASS (hidden: rows match)

- 66 tokens in 7.6s, finish: stop
- verifier: pass

```sql
SELECT strftime('%Y-%m', placed_on) AS month, SUM(amount) AS total_amount
FROM orders
WHERE strftime('%Y', placed_on) = '2024'
GROUP BY strftime('%Y-%m', placed_on)
HAVING total_amount > 0
ORDER BY month;
```
