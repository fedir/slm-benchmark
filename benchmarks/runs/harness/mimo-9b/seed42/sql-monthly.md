# mimo-9b / sql-monthly / seed 42 / harness

## Prompt

Tables `customers(id INTEGER PRIMARY KEY, name TEXT)` and `orders(id INTEGER PRIMARY KEY, customer_id INTEGER, amount INTEGER, placed_on TEXT)` (`placed_on` is 'YYYY-MM-DD'). Write one SQLite query that returns the total order amount per month (as 'YYYY-MM') for orders placed in 2024, only for months that have orders, ordered by month. Reply with ONLY the SQL query in a code block.

## Attempt 1: PASS (hidden: rows match)

- 53 tokens in 17.7s, finish: stop
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
