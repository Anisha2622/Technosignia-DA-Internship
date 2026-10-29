"""
Day 11 — Data Visualization with Matplotlib and Seaborn
Beginner-friendly chart examples using fictional monthly business data.

Install if needed:
    python -m pip install pandas matplotlib seaborn
Keep this script and day11_visualization_sample_data.csv in the same folder.
Run:
    python day11_data_visualization.py
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("day11_visualization_sample_data.csv")
sns.set_theme()  # Use a clean default chart style.

# 1. Bar chart: compare sales by month.
plt.figure(figsize=(8, 4))
sns.barplot(data=df, x="month", y="sales", color="steelblue")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.tight_layout()
plt.show()
print("Observation 1: Sales increased overall from January to June, with the highest sales in June.")

# 2. Line chart: view the sales trend over time.
plt.figure(figsize=(8, 4))
sns.lineplot(data=df, x="month", y="sales", marker="o", label="Sales", color="steelblue")
plt.title("Sales Trend by Month")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.legend(title="Metric")
plt.tight_layout()
plt.show()
print("Observation 2: The line shows an overall upward sales trend, with a small dip in March.")

# 3. Histogram: inspect the distribution of order counts.
plt.figure(figsize=(8, 4))
sns.histplot(data=df, x="orders", bins=5, kde=True, color="steelblue")
plt.title("Distribution of Monthly Orders")
plt.xlabel("Orders")
plt.ylabel("Number of Months")
plt.tight_layout()
plt.show()
print("Observation 3: Order counts are spread across the observed range and tend to be higher in the later months.")

# 4. Box plot: identify the spread of sales values and possible unusual values.
plt.figure(figsize=(7, 4))
sns.boxplot(data=df, y="sales", color="steelblue")
plt.title("Spread of Monthly Sales")
plt.ylabel("Sales (₹)")
plt.tight_layout()
plt.show()
print("Observation 4: The box plot summarises the middle 50% of sales and helps check for potential outliers; with only six months, interpret cautiously.")

# 5. Scatter plot: explore the relationship between advertising spend and sales.
plt.figure(figsize=(8, 4))
sns.scatterplot(data=df, x="advertising_spend", y="sales", hue="month", s=100)
plt.title("Advertising Spend vs Sales")
plt.xlabel("Advertising Spend (₹)")
plt.ylabel("Sales (₹)")
plt.legend(title="Month")
plt.tight_layout()
plt.show()
print("Observation 5: Higher advertising spend coincides with higher sales in this small sample, but this does not prove advertising caused the increase.")

# 6. Correlation heatmap: inspect relationships between numeric variables.
numeric_df = df[["sales", "orders", "advertising_spend", "customer_satisfaction"]]
correlation = numeric_df.corr(numeric_only=True)
plt.figure(figsize=(7, 5))
sns.heatmap(correlation, annot=True, cmap="coolwarm", vmin=-1, vmax=1, fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
print("Observation 6: The heatmap shows positive correlations among several variables in this sample. Correlation indicates association, not causation.")
