"""
Day 5 — NumPy for Numerical Computing
Run: python day5_numpy_numerical_computing.py

Requires NumPy. Install if needed:
    python -m pip install numpy
"""

import numpy as np

print("1. ARRAYS")
daily_sales = np.array([120, 250, 180, 90, 300])
print("One-dimensional array:", daily_sales)
weekly_sales = np.array([[120, 250, 180], [90, 300, 210]])
print("Two-dimensional array:")
print(weekly_sales)
print("Shape:", weekly_sales.shape)

print("\n2. INDEXING AND SLICING")
numbers = np.array([10, 20, 30, 40, 50, 60])
print("First value:", numbers[0])
print("Values at index 1 to 3:", numbers[1:4])

print("\n3. FILTERING")
sales = np.array([120, 250, 180, 90, 300, 140])
print("Sales greater than 150:", sales[sales > 150])

print("\n4. RESHAPING")
values = np.array([1, 2, 3, 4, 5, 6])
print(values.reshape(2, 3))

print("\n5. SUMMARY STATISTICS")
marks = np.array([70, 85, 90, 65, 80])
print("Sum:", np.sum(marks))
print("Mean:", np.mean(marks))
print("Minimum:", np.min(marks))
print("Maximum:", np.max(marks))
print("Standard deviation:", np.std(marks))

print("\n6. PYTHON LIST VS NUMPY")
python_numbers = [10, 20, 30, 40]
print("Python list + 5:", [number + 5 for number in python_numbers])
numpy_numbers = np.array(python_numbers)
print("NumPy array + 5:", numpy_numbers + 5)

print("\n7. PRACTICAL SALES EXAMPLE")
daily_sales = np.array([1200, 1500, 900, 1800, 1600, 1100, 2000])
average_sales = np.mean(daily_sales)
print("Daily sales:", daily_sales)
print("Average sales:", average_sales)
print("Sales above average:", daily_sales[daily_sales > average_sales])
print("Highest daily sales:", np.max(daily_sales))
