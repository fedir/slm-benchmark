# qwen2.5-coder-3b / sql-monthly / seed 45 / harness

## Prompt

Tables `customers(id INTEGER PRIMARY KEY, name TEXT)` and `orders(id INTEGER PRIMARY KEY, customer_id INTEGER, amount INTEGER, placed_on TEXT)` (`placed_on` is 'YYYY-MM-DD'). Write one SQLite query that returns the total order amount per month (as 'YYYY-MM') for orders placed in 2024, only for months that have orders, ordered by month. Reply with ONLY the SQL query in a code block.

## Attempt 1: FAIL (hidden: the query fails: OperationalError: no such function: DATE_TRUNC)

- 65 tokens in 7.2s, finish: stop
- verifier: FAIL: on a small example table the query the query fails: OperationalError: no such function: DATE_TRUNC

```sql
SELECT DATE_TRUNC('month', placed_on) AS month, SUM(amount) AS total_amount
FROM orders
WHERE DATE_PART('year', placed_on) = 2024
GROUP BY DATE_TRUNC('month', placed_on)
HAVING COUNT(*) > 0
ORDER BY month;
```

## Attempt 2: FAIL (hidden: returned [] (0 rows), expected [('2024-01', 150), ('2024-02', 70), ('2024-03', 210)] (3 rows))

- 72 tokens in 9.2s, finish: stop
- verifier: FAIL: on a small example table the query returned [] (0 rows), expected [('2024-07', 11), ('2024-09', 9)] (2 rows)

```sql
SELECT STRFTIME('%Y-%m', placed_on) AS month, SUM(amount) AS total_amount
FROM orders
WHERE STRFTIME('%Y', placed_on) = 2024
GROUP BY STRFTIME('%Y-%m', placed_on)
HAVING COUNT(*) > 0
ORDER BY month;
```

## Attempt 3: FAIL (hidden: the query fails: OperationalError: no such function: DATE_FORMAT)

- 72 tokens in 10.4s, finish: stop
- verifier: FAIL: on a small example table the query the query fails: OperationalError: no such function: DATE_FORMAT

```sql
SELECT DATE_FORMAT(placed_on, '%Y-%m') AS month, SUM(amount) AS total_amount
FROM orders
WHERE DATE_FORMAT(placed_on, '%Y') = '2024'
GROUP BY DATE_FORMAT(placed_on, '%Y-%m')
HAVING COUNT(*) > 0
ORDER BY month;
```
