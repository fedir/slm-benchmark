# ornith-9b-mtp / sql-monthly / seed 46 / harness

## Prompt

Tables `customers(id INTEGER PRIMARY KEY, name TEXT)` and `orders(id INTEGER PRIMARY KEY, customer_id INTEGER, amount INTEGER, placed_on TEXT)` (`placed_on` is 'YYYY-MM-DD'). Write one SQLite query that returns the total order amount per month (as 'YYYY-MM') for orders placed in 2024, only for months that have orders, ordered by month. Reply with ONLY the SQL query in a code block.

## Attempt 1: PASS (hidden: rows match)

- 65 tokens in 15.3s, finish: stop
- verifier: pass

```sql
SELECT 
    substr(placed_on, 1, 7) AS month,
    SUM(amount) AS total_amount
FROM orders
WHERE placed_on LIKE '2024-%'
GROUP BY substr(placed_on, 1, 7)
ORDER BY month;
```
