# gemma-4-e4b-terse / sql-monthly / seed 42 / harness

## Prompt

Tables `customers(id INTEGER PRIMARY KEY, name TEXT)` and `orders(id INTEGER PRIMARY KEY, customer_id INTEGER, amount INTEGER, placed_on TEXT)` (`placed_on` is 'YYYY-MM-DD'). Write one SQLite query that returns the total order amount per month (as 'YYYY-MM') for orders placed in 2024, only for months that have orders, ordered by month. Reply with ONLY the SQL query in a code block.

## Attempt 1: PASS (hidden: rows match)

- 50 tokens in 11.4s, finish: stop
- verifier: pass

```sqlite
SELECT strftime('%Y-%m', placed_on), SUM(amount) FROM orders WHERE strftime('%Y', placed_on) = '2024' GROUP BY 1 ORDER BY 1;
```
