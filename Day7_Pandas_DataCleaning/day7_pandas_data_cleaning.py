"""
Day 7 — Pandas II: Data Cleaning

This beginner-friendly script demonstrates:
- identifying and handling missing values
- detecting duplicate records
- correcting data types
- standardising text categories
- converting date strings to datetime values
- comparing data before and after cleaning

Keep this script and day7_sales_data_unclean.csv in the same folder.
Run: python day7_pandas_data_cleaning.py

Install dependencies if needed:
    python -m pip install pandas
"""

from pathlib import Path
import pandas as pd

DATA_FILE = Path(__file__).with_name("day7_sales_data_unclean.csv")
OUTPUT_FILE = Path(__file__).with_name("day7_sales_data_cleaned.csv")


def clean_sales_data(data):
    """Return a cleaned copy of the input DataFrame."""
    cleaned = data.copy()

    # Remove extra spaces from text fields.
    for column in ["customer", "category"]:
        cleaned[column] = cleaned[column].astype("string").str.strip()

    # Treat blank customer/category values as missing.
    cleaned["customer"] = cleaned["customer"].replace("", pd.NA)
    cleaned["category"] = cleaned["category"].replace("", pd.NA)

    # Standardise category labels so values such as 'stationery' and
    # 'Stationery ' use one consistent form.
    cleaned["category"] = cleaned["category"].str.title()

    # Convert numeric columns; invalid text becomes a missing value.
    cleaned["quantity"] = pd.to_numeric(cleaned["quantity"], errors="coerce")
    cleaned["unit_price"] = pd.to_numeric(cleaned["unit_price"], errors="coerce")

    # Convert mixed date formats; values that cannot be interpreted become NaT.
    cleaned["order_date"] = pd.to_datetime(
        cleaned["order_date"], errors="coerce", format="mixed"
    )

    # Remove exact duplicate rows after trimming whitespace and standardising text.
    before_deduplication = len(cleaned)
    cleaned = cleaned.drop_duplicates()
    duplicates_removed = before_deduplication - len(cleaned)

    # For this practice dataset, keep records only when essential values exist.
    # We do not invent missing quantities, prices, customers, or dates.
    essential_columns = ["customer", "category", "quantity", "unit_price", "order_date"]
    before_missing_removal = len(cleaned)
    cleaned = cleaned.dropna(subset=essential_columns)
    rows_missing_essential_values_removed = before_missing_removal - len(cleaned)

    # Use integer quantities after rows with missing/invalid quantities are removed.
    cleaned["quantity"] = cleaned["quantity"].astype(int)

    # Add a useful calculated column for later analysis.
    cleaned["line_total"] = cleaned["quantity"] * cleaned["unit_price"]

    cleaning_summary = {
        "duplicates_removed": duplicates_removed,
        "rows_removed_for_missing_or_invalid_essential_values": rows_missing_essential_values_removed,
    }
    return cleaned, cleaning_summary


def main():
    try:
        if not DATA_FILE.exists():
            print(f"Could not find {DATA_FILE.name}. Keep it beside this script.")
            return

        raw = pd.read_csv(DATA_FILE)
        print("BEFORE CLEANING")
        print("-" * 40)
        print("Rows and columns:", raw.shape)
        print("Missing values by column:")
        print(raw.isna().sum())
        print("Exact duplicate rows:", raw.duplicated().sum())
        print("\\nData types:")
        print(raw.dtypes)

        cleaned, summary = clean_sales_data(raw)

        print("\\nAFTER CLEANING")
        print("-" * 40)
        print("Rows and columns:", cleaned.shape)
        print("Missing values by column:")
        print(cleaned.isna().sum())
        print("Exact duplicate rows:", cleaned.duplicated().sum())
        print("\\nData types:")
        print(cleaned.dtypes)
        print("\\nCleaning summary:", summary)
        print("\\nCleaned data preview:")
        print(cleaned.head())

        cleaned.to_csv(OUTPUT_FILE, index=False)
        print(f"\\nCleaned dataset saved as: {OUTPUT_FILE.name}")

    except (OSError, pd.errors.EmptyDataError, pd.errors.ParserError) as error:
        print("There was a problem reading or writing the file:", error)


if __name__ == "__main__":
    main()
