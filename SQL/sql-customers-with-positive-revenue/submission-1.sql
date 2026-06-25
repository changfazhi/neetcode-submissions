-- Write your query below
SELECT DISTINCT customer_id
FROM customers
WHERE revenue > 0 and year = 2020
