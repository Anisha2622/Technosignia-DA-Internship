# Day 15 — SQL Query Explanations

Use these SQLite-style queries after importing `day15_assessment_sales.csv` into a table named `sales`.

## Query 1 — View the first five records

```sql
SELECT *
FROM sales
LIMIT 5;
```

**Explanation:** `SELECT *` asks SQL to show every column. `FROM sales` tells SQL which table to read. `LIMIT 5` restricts the output to five rows. This is useful for quickly checking whether the table imported correctly.

**What it tells us:** Expected meaning: Displays the first five sales records, including their IDs, dates, products, quantities, and sales values.

## Query 2 — Calculate total sales and total profit

```sql
SELECT SUM(Sales) AS total_sales,
       SUM(Profit) AS total_profit
FROM sales;
```

**Explanation:** `SUM(Sales)` adds all values in the Sales column. `SUM(Profit)` adds all profit values. `AS` gives each result a clear output name. There is no GROUP BY, so SQL returns one overall summary row.

**What it tells us:** Expected meaning: Shows the total revenue and total profit across all records in the dataset.

## Query 3 — Sales by product category

```sql
SELECT Category, SUM(Sales) AS category_sales
FROM sales
GROUP BY Category
ORDER BY category_sales DESC;
```

**Explanation:** `Category` identifies each category. `GROUP BY Category` combines rows belonging to the same category. `SUM(Sales)` calculates each category's total sales. `ORDER BY ... DESC` sorts from highest to lowest sales.

**What it tells us:** Expected meaning: Helps identify which product category generates the most sales.

## Query 4 — Sales by city

```sql
SELECT City, SUM(Sales) AS city_sales
FROM sales
GROUP BY City
ORDER BY city_sales DESC;
```

**Explanation:** This query groups sales records by city and adds the sales values in each city. The DESC sort places the city with the highest total at the top.

**What it tells us:** Expected meaning: Helps compare sales performance across cities.

## Query 5 — Monthly sales

```sql
SELECT strftime('%Y-%m', SaleDate) AS sale_month,
       SUM(Sales) AS monthly_sales
FROM sales
GROUP BY sale_month
ORDER BY sale_month;
```

**Explanation:** `strftime('%Y-%m', SaleDate)` extracts the year and month from each date in SQLite, such as `2026-01`. SQL groups records by that month and adds their sales. `ORDER BY sale_month` lists months chronologically.

**What it tells us:** Expected meaning: Shows how sales change from month to month. This helps identify increases or decreases over time.

## Query 6 — Products with more than five units sold

```sql
SELECT Product, SUM(Quantity) AS units_sold
FROM sales
GROUP BY Product
HAVING SUM(Quantity) > 5
ORDER BY units_sold DESC;
```

**Explanation:** `SUM(Quantity)` totals the units sold for each product. `GROUP BY Product` makes one group per product. `HAVING` filters groups after aggregation, so only products with more than five total units appear. `ORDER BY` ranks them by units sold.

**What it tells us:** Expected meaning: Finds products whose combined quantity sold is greater than five. `HAVING` is used here because the condition depends on a total.

## Query 7 — Compare online and store sales

```sql
SELECT SalesChannel, SUM(Sales) AS channel_sales
FROM sales
GROUP BY SalesChannel
ORDER BY channel_sales DESC;
```

**Explanation:** The query groups the records by SalesChannel, such as Online or Store, and calculates total sales for each channel. Results are sorted from highest to lowest.

**What it tells us:** Expected meaning: Helps compare revenue from online sales with revenue from store sales.

## Query 8 — Average sales per record

```sql
SELECT AVG(Sales) AS average_sales
FROM sales;
```

**Explanation:** `AVG(Sales)` calculates the arithmetic average of the Sales column. SQL ignores NULL values when calculating AVG. The alias `average_sales` makes the result easier to understand.

**What it tells us:** Expected meaning: Shows the average sales value for one row/transaction in this dataset. It is not necessarily the average per customer because customer IDs are not included.

## Query 9 — Check missing values in important columns

```sql
SELECT
    SUM(CASE WHEN SaleID IS NULL OR SaleID = '' THEN 1 ELSE 0 END) AS missing_sale_id,
    SUM(CASE WHEN Product IS NULL OR Product = '' THEN 1 ELSE 0 END) AS missing_product,
    SUM(CASE WHEN Sales IS NULL THEN 1 ELSE 0 END) AS missing_sales
FROM sales;
```

**Explanation:** `CASE WHEN` checks a condition. If a value is NULL or an empty string, it returns 1; otherwise it returns 0. `SUM` adds these flags to count missing values in each selected column. This is a basic data-quality check.

**What it tells us:** Expected meaning: Returns counts of missing sale IDs, product names, and sales values. A result of 0 means no missing values were found in that column.

## Query 10 — Find duplicate sale IDs

```sql
SELECT SaleID, COUNT(*) AS record_count
FROM sales
GROUP BY SaleID
HAVING COUNT(*) > 1;
```

**Explanation:** `GROUP BY SaleID` creates a group for each sale ID. `COUNT(*)` counts how many rows have that ID. `HAVING COUNT(*) > 1` keeps only IDs that occur more than once.

**What it tells us:** Expected meaning: If the query returns no rows, no duplicate SaleID values were found. Duplicate IDs should be investigated before removing records.

## One query to explain to the mentor

The category sales query groups records by category, sums the sales in each group, and sorts the totals from highest to lowest. It helps identify the category with the highest sales.
