# ornith-9b-mtp / sql-monthly / seed 45 / harness

## Prompt

Tables `customers(id INTEGER PRIMARY KEY, name TEXT)` and `orders(id INTEGER PRIMARY KEY, customer_id INTEGER, amount INTEGER, placed_on TEXT)` (`placed_on` is 'YYYY-MM-DD'). Write one SQLite query that returns the total order amount per month (as 'YYYY-MM') for orders placed in 2024, only for months that have orders, ordered by month. Reply with ONLY the SQL query in a code block.

## Attempt 1: FAIL (hidden: returned [] (0 rows), expected [('2024-01', 150), ('2024-02', 70), ('2024-03', 210)] (3 rows))

- 54 tokens in 13.1s, finish: stop
- verifier: FAIL: on a small example table the query returned [] (0 rows), expected [('2024-07', 11), ('2024-09', 9)] (2 rows)

```sql
SELECT strftime('%Y-%m', placed_on) AS month, SUM(amount) AS total
FROM orders
WHERE strftime('%Y-%m', placed_on) = '2024'
GROUP BY month
ORDER BY month;
```

## Attempt 2: PASS (hidden: rows match)

- 58 tokens in 21.4s, finish: stop
- verifier: pass

```sql
SELECT substr(placed_on, 1, 7) AS month, SUM(amount) AS total
FROM orders
WHERE substr(placed_on, 1, 4) = '2024'
GROUP BY month
ORDER BY month;
```
