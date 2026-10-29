"""
Day 10 — Statistics for Data Analytics and Data Science
Beginner-friendly examples using Python, pandas, and NumPy.

Install if needed:
    python -m pip install pandas numpy matplotlib
Run:
    python day10_statistics_for_data_analytics.py
"""

import pandas as pd
import numpy as np

# Sample data: monthly sales contains a deliberately high outlier.
df = pd.read_csv("day10_statistics_sample_data.csv")

print("SAMPLE DATA")
print(df)

sales = df["monthly_sales"]

print("\n1. MEAN, MEDIAN, AND MODE")
print("Mean sales:", sales.mean())
print("Median sales:", sales.median())
print("Mode sales:", sales.mode().tolist())

print("\n2. VARIANCE AND STANDARD DEVIATION")
print("Sample variance:", sales.var())
print("Sample standard deviation:", sales.std())
print("Note: pandas uses sample variance and standard deviation by default (ddof=1).")

print("\n3. QUARTILES AND PERCENTILES")
print("25th percentile (Q1):", sales.quantile(0.25))
print("50th percentile (median):", sales.quantile(0.50))
print("75th percentile (Q3):", sales.quantile(0.75))
print("90th percentile:", sales.quantile(0.90))

print("\n4. OUTLIERS USING THE IQR METHOD")
q1 = sales.quantile(0.25)
q3 = sales.quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers = df[(sales < lower_bound) | (sales > upper_bound)]
print("Q1:", q1, "Q3:", q3, "IQR:", iqr)
print("Lower bound:", lower_bound, "Upper bound:", upper_bound)
print("Possible outlier rows:")
print(outliers[["employee_id", "monthly_sales"]])

print("\n5. DISTRIBUTION AND OUTLIER COMPARISON")
regular_sales = sales[sales < upper_bound]
print("Mean including all values:", sales.mean())
print("Median including all values:", sales.median())
print("Mean after excluding the detected outlier for comparison:", regular_sales.mean())
print("Median after excluding the detected outlier for comparison:", regular_sales.median())
print("Important: do not remove an outlier from real data without checking whether it is an error or a genuine event.")

print("\n6. CORRELATION")
print(df[["hours_studied", "exam_score", "monthly_sales"]].corr(numeric_only=True))
print("Correlation shows association, not proof that one variable causes another.")

print("\n7. QUICK DESCRIPTIVE SUMMARY")
print(df[["hours_studied", "exam_score", "monthly_sales"]].describe())
