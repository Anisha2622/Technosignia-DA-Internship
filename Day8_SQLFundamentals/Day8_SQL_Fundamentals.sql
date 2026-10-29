-- Day 8 — SQL Fundamentals
-- Beginner-friendly practice queries for a small sales database.
-- Works in SQLite. Run this entire file in DB Browser for SQLite or the sqlite3 CLI.
-- The setup section creates sample tables and data so the queries can be practised immediately.

-- ------------------------------------------------------------
-- 1. Create sample tables
-- ------------------------------------------------------------
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

-- ------------------------------------------------------------
-- 2. Insert fictional sample data
-- ------------------------------------------------------------
INSERT INTO customers (customer_id, customer_name, city) VALUES
(1, 'Asha Patil', 'Pune'),
(2, 'Rahul Shah', 'Mumbai'),
(3, 'Meera Joshi', 'Satara'),
(4, 'Kabir Khan', NULL),
(5, 'Sana More', 'Pune');

INSERT INTO products (product_id, product_name, category, price) VALUES
(101, 'Notebook', 'Stationery', 40.00),
(102, 'Pen', 'Stationery', 10.00),
(103, 'Water Bottle', 'Accessories', 150.00),
(104, 'Lunch Box', 'Accessories', 220.00),
(105, 'Pencil', 'Stationery', 5.00);

INSERT INTO sales (sale_id, customer_id, product_id, quantity, sale_date) VALUES
(1001, 1, 101, 3, '2026-10-01'),
(1002, 2, 102, 10, '2026-10-02'),
(1003, 1, 103, 2, '2026-10-03'),
(1004, 3, 104, 1, '2026-10-04'),
(1005, 5, 105, 12, '2026-10-05'),
(1006, 4, 101, 2, '2026-10-06'),
(1007, 2, 103, 1, '2026-10-07'),
(1008, 3, 102, 5, '2026-10-08');

-- ------------------------------------------------------------
-- 3. Practice queries (at least 10, each with a short explanation)
-- ------------------------------------------------------------

-- Query 1: Show every customer.
-- SELECT * returns all columns from the selected table.
SELECT * FROM customers;

-- Query 2: Select only customer names and cities.
-- Use this when you only need particular columns.
SELECT customer_name, city
FROM customers;

-- Query 3: Filter customers who live in Pune.
-- WHERE keeps only rows that match the condition.
SELECT *
FROM customers
WHERE city = 'Pune';

-- Query 4: Find products that cost more than Rs. 50.
-- A comparison operator filters by price.
SELECT product_name, price
FROM products
WHERE price > 50;

-- Query 5: Sort products from highest price to lowest.
-- ORDER BY DESC sorts in descending order.
SELECT product_name, price
FROM products
ORDER BY price DESC;

-- Query 6: Show each product category only once.
-- DISTINCT removes repeated values from the result.
SELECT DISTINCT category
FROM products;

-- Query 7: Use aliases to make column headings easier to read.
-- AS gives a temporary name to a column in the result.
SELECT customer_name AS customer, city AS customer_city
FROM customers;

-- Query 8: Find customers whose city is missing.
-- Use IS NULL, not = NULL, to check for missing SQL values.
SELECT *
FROM customers
WHERE city IS NULL;

-- Query 9: Find customers whose city is known.
-- IS NOT NULL returns rows where the field has a value.
SELECT *
FROM customers
WHERE city IS NOT NULL;

-- Query 10: Find sales with a quantity of at least 5.
SELECT *
FROM sales
WHERE quantity >= 5;

-- Query 11: Combine conditions using AND.
-- Both conditions must be true.
SELECT *
FROM products
WHERE category = 'Stationery' AND price < 20;

-- Query 12: Combine conditions using OR.
-- At least one condition must be true.
SELECT *
FROM customers
WHERE city = 'Pune' OR city = 'Satara';

-- Query 13: Show sales records with readable customer and product names.
-- JOIN connects related tables through their IDs.
SELECT sales.sale_id, customers.customer_name, products.product_name,
       sales.quantity, sales.sale_date
FROM sales
JOIN customers ON sales.customer_id = customers.customer_id
JOIN products ON sales.product_id = products.product_id
ORDER BY sales.sale_date;

-- Query 14: Calculate the value of each sale.
-- Multiply quantity by product price to estimate each sale line's value.
SELECT sales.sale_id, products.product_name, sales.quantity,
       products.price, sales.quantity * products.price AS sale_total
FROM sales
JOIN products ON sales.product_id = products.product_id
ORDER BY sales.sale_id;

-- Query 15: Find sales made on or after 2026-10-05.
-- ISO-style YYYY-MM-DD dates sort correctly as text in this sample.
SELECT *
FROM sales
WHERE sale_date >= '2026-10-05'
ORDER BY sale_date;

-- Query 16: Count how many customers are in each city.
-- COUNT(*) counts rows; GROUP BY makes one result per city.
SELECT city, COUNT(*) AS customer_count
FROM customers
GROUP BY city
ORDER BY customer_count DESC;

-- Query 17: Count sales records.
SELECT COUNT(*) AS total_sales_records
FROM sales;

-- Query 18: Search for product names containing the word 'Bottle'.
-- LIKE supports simple text pattern matching.
SELECT *
FROM products
WHERE product_name LIKE '%Bottle%';

-- End of Day 8 practice file.
