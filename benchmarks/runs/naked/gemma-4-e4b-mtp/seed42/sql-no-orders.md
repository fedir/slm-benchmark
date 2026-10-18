# gemma-4-e4b-mtp / sql-no-orders / seed 42 / naked

## Prompt

Tables `customers(id INTEGER PRIMARY KEY, name TEXT)` and `orders(id INTEGER PRIMARY KEY, customer_id INTEGER, amount INTEGER, placed_on TEXT)` (`placed_on` is 'YYYY-MM-DD'). Write one SQLite query that returns the names of customers who have placed no orders, ordered by name. Reply with ONLY the SQL query in a code block.

## Attempt 1: PASS (hidden: rows match)

- 60 tokens in 10.2s, finish: stop

```sqlite
SELECT
  T1.name
FROM customers AS T1
LEFT JOIN orders AS T2
  ON T1.id = T2.customer_id
WHERE
  T2.id IS NULL
ORDER BY
  T1.name;
```
