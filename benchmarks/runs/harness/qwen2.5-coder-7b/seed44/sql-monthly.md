# qwen2.5-coder-7b / sql-monthly / seed 44 / harness

## Prompt

Tables `customers(id INTEGER PRIMARY KEY, name TEXT)` and `orders(id INTEGER PRIMARY KEY, customer_id INTEGER, amount INTEGER, placed_on TEXT)` (`placed_on` is 'YYYY-MM-DD'). Write one SQLite query that returns the total order amount per month (as 'YYYY-MM') for orders placed in 2024, only for months that have orders, ordered by month. Reply with ONLY the SQL query in a code block.

## Attempt 1: FAIL (hidden: returned [('2024-01-05', 150), ('2024-02-11', 70), ('2024-03-01', 210)] (3 rows), expected [('2024-01', 150), ('2024-02', 70), ('2024-03', 210)] (3 rows))

- 65 tokens in 16.0s, finish: stop
- verifier: FAIL: on a small example table the query returned [('2024-07-01', 11), ('2024-09-09', 9)] (2 rows), expected [('2024-07', 11), ('2024-09', 9)] (2 rows)

```sql
SELECT 
    placed_on,
    SUM(amount) AS total_amount
FROM 
    orders
WHERE 
    STRFTIME('%Y', placed_on) = '2024'
GROUP BY 
    STRFTIME('%Y-%m', placed_on)
ORDER BY 
    placed_on;
```

## Attempt 2: PASS (hidden: rows match)

- 66 tokens in 20.6s, finish: stop
- verifier: pass

```sql
SELECT 
    STRFTIME('%Y-%m', placed_on) AS month,
    SUM(amount) AS total_amount
FROM 
    orders
WHERE 
    STRFTIME('%Y', placed_on) = '2024'
GROUP BY 
    month
ORDER BY 
    month;
```
