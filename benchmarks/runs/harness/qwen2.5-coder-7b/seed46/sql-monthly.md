# qwen2.5-coder-7b / sql-monthly / seed 46 / harness

## Prompt

Tables `customers(id INTEGER PRIMARY KEY, name TEXT)` and `orders(id INTEGER PRIMARY KEY, customer_id INTEGER, amount INTEGER, placed_on TEXT)` (`placed_on` is 'YYYY-MM-DD'). Write one SQLite query that returns the total order amount per month (as 'YYYY-MM') for orders placed in 2024, only for months that have orders, ordered by month. Reply with ONLY the SQL query in a code block.

## Attempt 1: FAIL (hidden: returned [('2024-01-05', 100), ('2024-01-20', 50), ('2024-02-11', 70), ('2024-03-01', 200), ('2024-03-15', 10)] (5 rows), expected [('2024-01', 150), ('2024-02', 70), ('2024-03', 210)] (3 rows))

- 40 tokens in 11.2s, finish: stop
- verifier: FAIL: on a small example table the query returned [('2024-07-01', 5), ('2024-07-30', 6), ('2024-09-09', 9)] (3 rows), expected [('2024-07', 11), ('2024-09', 9)] (2 rows)

```sql
SELECT placed_on, SUM(amount) AS total_amount
FROM orders
WHERE placed_on LIKE '2024-%'
GROUP BY placed_on
ORDER BY placed_on;
```

## Attempt 2: FAIL (hidden: the query fails: OperationalError: no such function: DATE_FORMAT)

- 49 tokens in 17.3s, finish: stop
- verifier: FAIL: on a small example table the query the query fails: OperationalError: no such function: DATE_FORMAT

```sql
SELECT DATE_FORMAT(placed_on, '%Y-%m') AS month, SUM(amount) AS total_amount
FROM orders
WHERE placed_on LIKE '2024-%'
GROUP BY month
ORDER BY month;
```

## Attempt 3: PASS (hidden: rows match)

- 49 tokens in 18.7s, finish: stop
- verifier: pass

```sql
SELECT substr(placed_on, 1, 7) AS month, SUM(amount) AS total_amount
FROM orders
WHERE placed_on LIKE '2024-%'
GROUP BY month
ORDER BY month;
```
