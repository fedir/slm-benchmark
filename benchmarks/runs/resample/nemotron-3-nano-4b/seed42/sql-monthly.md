# nemotron-3-nano-4b / sql-monthly / seed 42 / resample (no feedback)

## Prompt

Tables `customers(id INTEGER PRIMARY KEY, name TEXT)` and `orders(id INTEGER PRIMARY KEY, customer_id INTEGER, amount INTEGER, placed_on TEXT)` (`placed_on` is 'YYYY-MM-DD'). Write one SQLite query that returns the total order amount per month (as 'YYYY-MM') for orders placed in 2024, only for months that have orders, ordered by month. Reply with ONLY the SQL query in a code block.

## Attempt 1: PASS (hidden: rows match)

- 81 tokens in 14.0s, finish: stop
- verifier: pass

```sql
SELECT 
    strftime('%Y-%m', orders.placed_on) AS month,
    SUM(orders.amount) AS total_amount
FROM orders
WHERE orders.placed_on >= '2024-01-01' AND orders.placed_on <= '2024-12-31'
GROUP BY month
ORDER BY month;
```
