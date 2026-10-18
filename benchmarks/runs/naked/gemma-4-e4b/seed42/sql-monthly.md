# gemma-4-e4b / sql-monthly / seed 42 / naked

## Prompt

Tables `customers(id INTEGER PRIMARY KEY, name TEXT)` and `orders(id INTEGER PRIMARY KEY, customer_id INTEGER, amount INTEGER, placed_on TEXT)` (`placed_on` is 'YYYY-MM-DD'). Write one SQLite query that returns the total order amount per month (as 'YYYY-MM') for orders placed in 2024, only for months that have orders, ordered by month. Reply with ONLY the SQL query in a code block.

## Attempt 1: PASS (hidden: rows match)

- 73 tokens in 13.2s, finish: stop

```sqlite
SELECT
  strftime('%Y-%m', placed_on) AS order_month,
  SUM(amount) AS total_amount
FROM orders
WHERE
  strftime('%Y', placed_on) = '2024'
GROUP BY
  order_month
ORDER BY
  order_month;
```
