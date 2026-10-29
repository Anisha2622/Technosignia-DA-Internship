"""
Day 6 — Pandas I: Data Loading and Exploration

Keep this script and day6_sample_sales.csv in the same folder.
Run: python day6_pandas_exploration.py

Install dependencies if needed:
    python -m pip install pandas openpyxl
"""

from pathlib import Path
import pandas as pd

data_file = Path(__file__).with_name("day6_sample_sales.csv")

try:
    df = pd.read_csv(data_file)

    print("First five rows:")
    print(df.head())

    print("\nLast three rows:")
    print(df.tail(3))

    print("\nDataset information:")
    df.info()

    print("\nShape (rows, columns):", df.shape)
    print("\nColumn data types:")
    print(df.dtypes)

    print("\nNumerical summary:")
    print(df.describe())

    print("\nMissing values by column:")
    print(df.isna().sum())

    print("\nDuplicate rows:", df.duplicated().sum())

    print("\nSelected columns:")
    print(df[["product", "quantity", "unit_price"]].head())

    df["line_total"] = df["quantity"] * df["unit_price"]
    print("\nTotal line value (known prices):", df["line_total"].sum(skipna=True))

except FileNotFoundError:
    print("CSV file not found. Keep day6_sample_sales.csv beside this script.")
except (pd.errors.EmptyDataError, pd.errors.ParserError) as error:
    print("Could not read the CSV file:", error)
