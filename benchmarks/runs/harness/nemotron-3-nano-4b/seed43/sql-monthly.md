# nemotron-3-nano-4b / sql-monthly / seed 43 / harness

## Prompt

Tables `customers(id INTEGER PRIMARY KEY, name TEXT)` and `orders(id INTEGER PRIMARY KEY, customer_id INTEGER, amount INTEGER, placed_on TEXT)` (`placed_on` is 'YYYY-MM-DD'). Write one SQLite query that returns the total order amount per month (as 'YYYY-MM') for orders placed in 2024, only for months that have orders, ordered by month. Reply with ONLY the SQL query in a code block.

## Attempt 1: FAIL (hidden: the query fails: OperationalError: no such function: year)

- 54 tokens in 10.2s, finish: stop
- verifier: FAIL: on a small example table the query the query fails: OperationalError: no such function: year

```sql
SELECT 
    strftime('%Y-%m', placed_on) AS month,
    SUM(amount) AS total_amount
FROM orders
WHERE year(placed_on) = 2024
GROUP BY month
ORDER BY month;
```

## Attempt 2: PASS (hidden: rows match)

- 52 tokens in 12.1s, finish: stop
- verifier: pass

```sql
SELECT 
    strftime('%Y-%m', placed_on) AS month,
    SUM(amount) AS total_amount
FROM orders
WHERE placed_on LIKE '2024-%'
GROUP BY month
ORDER BY month;
```
