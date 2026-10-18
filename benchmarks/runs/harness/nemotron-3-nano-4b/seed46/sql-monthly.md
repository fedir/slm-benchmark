# nemotron-3-nano-4b / sql-monthly / seed 46 / harness

## Prompt

Tables `customers(id INTEGER PRIMARY KEY, name TEXT)` and `orders(id INTEGER PRIMARY KEY, customer_id INTEGER, amount INTEGER, placed_on TEXT)` (`placed_on` is 'YYYY-MM-DD'). Write one SQLite query that returns the total order amount per month (as 'YYYY-MM') for orders placed in 2024, only for months that have orders, ordered by month. Reply with ONLY the SQL query in a code block.

## Attempt 1: FAIL (hidden: the query fails: OperationalError: no such function: DATE_FORMAT)

- 70 tokens in 12.5s, finish: stop
- verifier: FAIL: on a small example table the query the query fails: OperationalError: no such function: DATE_FORMAT

```sql
SELECT DATE_FORMAT(placed_on, '%Y-%m') AS month, SUM(amount) AS total_amount
FROM orders
WHERE placed_on >= '2024-01-01' AND placed_on <= '2024-12-31'
GROUP BY month
ORDER BY month;
```

## Attempt 2: FAIL (hidden: the query fails: OperationalError: no such function: YEAR)

- 82 tokens in 16.3s, finish: stop
- verifier: FAIL: on a small example table the query the query fails: OperationalError: no such function: YEAR

```sql
SELECT YEAR(placed_on) || '-' || LPAD(MONTH(placed_on), 2, '0') AS month, SUM(amount) AS total_amount
FROM orders
WHERE placed_on >= '2024-01-01' AND placed_on <= '2024-12-31'
GROUP BY month
ORDER BY month;
```

## Attempt 3: FAIL (hidden: the query fails: OperationalError: no such function: MONTH)

- 80 tokens in 19.1s, finish: stop
- verifier: FAIL: on a small example table the query the query fails: OperationalError: no such function: MONTH

```sql
SELECT '2024-' || LPAD(MONTH(placed_on), 2, '0') AS month, SUM(amount) AS total_amount
FROM orders
WHERE placed_on >= '2024-01-01' AND placed_on <= '2024-12-31'
GROUP BY month
ORDER BY month;
```
