"""
Day 4 — Python File Handling and Error Handling

This script reads a CSV file, checks whether it exists, validates values,
calculates sales totals, and handles common errors.

Run:
    python day4_file_and_error_handling.py

Keep day4_sales_data.csv in the same folder as this script.
"""

import csv
from pathlib import Path

# Build a file path relative to this script, so it works from different folders.
DATA_FILE = Path(__file__).with_name("day4_sales_data.csv")


def process_sales_csv(file_path):
    """Read valid sales rows from a CSV file and print a simple summary."""
    total_sales = 0.0
    valid_rows = 0
    skipped_rows = 0

    try:
        # Check whether the CSV file exists before opening it.
        if not file_path.exists():
            raise FileNotFoundError(f"Could not find the file: {file_path.name}")

        # Use with so Python closes the file after reading it.
        with file_path.open(mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            required_columns = {"product", "quantity", "unit_price"}
            if not reader.fieldnames or not required_columns.issubset(set(reader.fieldnames)):
                raise ValueError(
                    "The CSV must contain these columns: product, quantity, unit_price."
                )

            print("Sales records:")
            for line_number, row in enumerate(reader, start=2):
                try:
                    product = (row.get("product") or "").strip()
                    quantity_text = (row.get("quantity") or "").strip()
                    price_text = (row.get("unit_price") or "").strip()

                    # Reject missing fields and invalid numeric values.
                    if not product or not quantity_text or not price_text:
                        raise ValueError("one or more required values are missing")

                    quantity = int(quantity_text)
                    unit_price = float(price_text)

                    if quantity < 0 or unit_price < 0:
                        raise ValueError("quantity and unit price must not be negative")

                    row_total = quantity * unit_price
                    total_sales += row_total
                    valid_rows += 1
                    print(
                        f"- {product}: {quantity} item(s) x Rs. {unit_price:.2f} "
                        f"= Rs. {row_total:.2f}"
                    )

                except ValueError as error:
                    skipped_rows += 1
                    print(f"Skipping row {line_number}: {error}")

        if valid_rows == 0:
            print("\nNo valid sales rows were found.")
        else:
            average_per_valid_row = total_sales / valid_rows
            print("\nSummary")
            print("-" * 30)
            print(f"Valid rows processed: {valid_rows}")
            print(f"Rows skipped: {skipped_rows}")
            print(f"Total sales: Rs. {total_sales:.2f}")
            print(f"Average sales per valid row: Rs. {average_per_valid_row:.2f}")

    except FileNotFoundError as error:
        print("File error:", error)
        print("Make sure day4_sales_data.csv is in the same folder as this script.")

    except (OSError, csv.Error) as error:
        print("There was a problem reading the CSV file:", error)

    except ValueError as error:
        print("CSV format error:", error)

    finally:
        # This block runs whether processing succeeds or an error occurs.
        print("\nCSV processing attempt finished.")


if __name__ == "__main__":
    process_sales_csv(DATA_FILE)
