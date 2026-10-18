# ornith-9b-mtp / sql-no-orders / seed 43 / harness

## Prompt

Tables `customers(id INTEGER PRIMARY KEY, name TEXT)` and `orders(id INTEGER PRIMARY KEY, customer_id INTEGER, amount INTEGER, placed_on TEXT)` (`placed_on` is 'YYYY-MM-DD'). Write one SQLite query that returns the names of customers who have placed no orders, ordered by name. Reply with ONLY the SQL query in a code block.

## Attempt 1: PASS (hidden: rows match)

- 28 tokens in 9.1s, finish: stop
- verifier: pass

```sql
SELECT name
FROM customers
WHERE id NOT IN (SELECT customer_id FROM orders)
ORDER BY name;
```
