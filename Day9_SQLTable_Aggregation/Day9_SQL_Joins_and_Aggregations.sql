-- DAY 9 — SQL Joins and Aggregations
-- Beginner-friendly intermediate SQL practice.
-- Compatible with SQLite. Creates fictional tables and sample data,
-- then demonstrates joins, aggregation, CASE WHEN, subqueries and a CTE.

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS sales;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS products;

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    city TEXT
);

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    category TEXT,
    price REAL
);

CREATE TABLE sales (
    sale_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    sale_date TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO customers (customer_id, customer_name, city) VALUES
(1, 'Asha Patil', 'Pune'),
(2, 'Rahul Shah', 'Mumbai'),
(3, 'Meera Joshi', 'Satara'),
(4, 'Kabir Khan', 'Pune'),
(5, 'Sana More', 'Mumbai'),
(6, 'Dev Kulkarni', 'Pune');

INSERT INTO products (product_id, product_name, category, price) VALUES
(101, 'Notebook', 'Stationery', 40.00),
(102, 'Pen', 'Stationery', 10.00),
(103, 'Water Bottle', 'Accessories', 150.00),
(104, 'Lunch Box', 'Accessories', 220.00),
(105, 'Pencil', 'Stationery', 5.00),
(106, 'Backpack', 'Bags', 650.00);

INSERT INTO sales (sale_id, customer_id, product_id, quantity, sale_date) VALUES
(1001, 1, 101, 3, '2026-10-01'),
(1002, 2, 102, 10, '2026-10-02'),
(1003, 1, 103, 2, '2026-10-03'),
(1004, 3, 104, 1, '2026-10-04'),
(1005, 5, 105, 12, '2026-10-05'),
(1006, 4, 101, 2, '2026-10-06'),
(1007, 2, 103, 1, '2026-10-07'),
(1008, 3, 102, 5, '2026-10-08'),
(1009, 1, 104, 2, '2026-11-02'),
(1010, 5, 103, 3, '2026-11-04'),
(1011, 2, 101, 4, '2026-11-10'),
(1012, 4, 105, 20, '2026-11-15');

-- QUERY 1: INNER JOIN — show only sales with matching customer and product records.
SELECT s.sale_id, c.customer_name, p.product_name, s.quantity, s.sale_date
FROM sales AS s
INNER JOIN customers AS c ON s.customer_id = c.customer_id
INNER JOIN products AS p ON s.product_id = p.product_id
ORDER BY s.sale_id;

-- QUERY 2: LEFT JOIN — list every customer, including those with no sales.
SELECT c.customer_id, c.customer_name, s.sale_id
FROM customers AS c
LEFT JOIN sales AS s ON c.customer_id = s.customer_id
ORDER BY c.customer_id, s.sale_id;

-- QUERY 3: GROUP BY — total quantity sold for each product.
SELECT p.product_name, SUM(s.quantity) AS total_quantity
FROM products AS p
LEFT JOIN sales AS s ON p.product_id = s.product_id
GROUP BY p.product_id, p.product_name
ORDER BY total_quantity DESC;

-- QUERY 4: Aggregates — calculate total, average, minimum and maximum product price.
SELECT SUM(price) AS sum_of_prices,
       AVG(price) AS average_price,
       MIN(price) AS minimum_price,
       MAX(price) AS maximum_price
FROM products;

-- QUERY 5: COUNT — count sales records per customer, including customers with zero sales.
SELECT c.customer_name, COUNT(s.sale_id) AS number_of_sales
FROM customers AS c
LEFT JOIN sales AS s ON c.customer_id = s.customer_id
GROUP BY c.customer_id, c.customer_name
ORDER BY number_of_sales DESC;

-- QUERY 6: HAVING — show customers whose total quantity sold is at least 5.
SELECT c.customer_name, SUM(s.quantity) AS total_quantity
FROM customers AS c
JOIN sales AS s ON c.customer_id = s.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING SUM(s.quantity) >= 5
ORDER BY total_quantity DESC;

-- QUERY 7: CASE WHEN — label products by price range.
SELECT product_name, price,
       CASE
           WHEN price >= 500 THEN 'High'
           WHEN price >= 100 THEN 'Medium'
           ELSE 'Low'
       END AS price_band
FROM products
ORDER BY price DESC;

-- QUERY 8: Subquery — find products priced above the average product price.
SELECT product_name, price
FROM products
WHERE price > (SELECT AVG(price) FROM products)
ORDER BY price DESC;

-- QUERY 9: Common Table Expression (CTE) — calculate revenue per sale first, then summarise by product.
WITH sale_values AS (
    SELECT s.sale_id, s.product_id, s.quantity * p.price AS revenue
    FROM sales AS s
    JOIN products AS p ON s.product_id = p.product_id
)
SELECT p.product_name, SUM(sv.revenue) AS total_revenue
FROM sale_values AS sv
JOIN products AS p ON sv.product_id = p.product_id
GROUP BY p.product_id, p.product_name
ORDER BY total_revenue DESC;

-- QUERY 10: Sales by customer — calculate the total value of purchases for each customer.
SELECT c.customer_name,
       SUM(s.quantity * p.price) AS total_purchase_value
FROM customers AS c
JOIN sales AS s ON c.customer_id = s.customer_id
JOIN products AS p ON s.product_id = p.product_id
GROUP BY c.customer_id, c.customer_name
ORDER BY total_purchase_value DESC;

-- QUERY 11: Sales by month — group sales by year-month.
SELECT substr(s.sale_date, 1, 7) AS sales_month,
       SUM(s.quantity * p.price) AS monthly_revenue
FROM sales AS s
JOIN products AS p ON s.product_id = p.product_id
GROUP BY substr(s.sale_date, 1, 7)
ORDER BY sales_month;

-- QUERY 12: Products with no sales — LEFT JOIN and NULL check.
SELECT p.product_name
FROM products AS p
LEFT JOIN sales AS s ON p.product_id = s.product_id
WHERE s.sale_id IS NULL;

-- QUERY 13: Compare each product's price with the average price using a scalar subquery.
SELECT product_name, price,
       (SELECT AVG(price) FROM products) AS overall_average_price
FROM products
ORDER BY price DESC;

-- QUERY 14: Category summary — count products and calculate average price per category.
SELECT category,
       COUNT(*) AS number_of_products,
       AVG(price) AS average_category_price
FROM products
GROUP BY category
ORDER BY number_of_products DESC;

-- QUERY 15: Conditional aggregation — count sales in October and November.
SELECT
    SUM(CASE WHEN substr(sale_date, 6, 2) = '10' THEN 1 ELSE 0 END) AS october_sales,
    SUM(CASE WHEN substr(sale_date, 6, 2) = '11' THEN 1 ELSE 0 END) AS november_sales
FROM sales;

-- END OF DAY 9 SQL PRACTICE
