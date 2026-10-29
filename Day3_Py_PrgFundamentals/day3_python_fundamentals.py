"""
Day 3 — Python Programming Fundamentals II
Examples: conditions, loops, collections, and functions.

Run: python day3_python_fundamentals.py
No external packages are required.
"""

print("EXERCISE 1: PASS OR NEEDS IMPROVEMENT")
marks = 72
if marks >= 40:
    print("Result: Pass")
else:
    print("Result: Needs improvement")

print("\nEXERCISE 2: GRADE")
marks = 82
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "Fail"
print("Marks:", marks, "| Grade:", grade)

print("\nEXERCISE 3: TOTAL SALES WITH FOR LOOP")
sales = [120, 250, 180, 90]
total = 0
for amount in sales:
    total += amount
print("Total sales:", total)

print("\nEXERCISE 4: WHILE LOOP")
number = 1
while number <= 5:
    print(number)
    number += 1

print("\nEXERCISE 5: LIST")
products = ["Notebook", "Pen", "Folder"]
products.append("Pencil")
print("Products:", products)

print("\nEXERCISE 6: TUPLE")
monthly_targets = (10000, 12000, 15000)
print("Monthly targets:", monthly_targets)
print("Second target:", monthly_targets[1])

print("\nEXERCISE 7: SET TO REMOVE DUPLICATES")
customer_ids = [101, 102, 101, 103, 102, 104]
unique_customer_ids = set(customer_ids)
print("Unique IDs:", unique_customer_ids)
print("Unique count:", len(unique_customer_ids))

print("\nEXERCISE 8: COUNT CATEGORIES WITH A DICTIONARY")
responses = ["Yes", "No", "Yes", "Maybe", "No", "Yes"]
counts = {}
for response in responses:
    if response in counts:
        counts[response] += 1
    else:
        counts[response] = 1
print("Response counts:", counts)

print("\nEXERCISE 9: FUNCTION TO CALCULATE TOTAL")
def calculate_total(prices):
    return sum(prices)
item_prices = [45, 30, 125, 50]
print("Total amount:", calculate_total(item_prices))

print("\nEXERCISE 10: FUNCTION TO FIND HIGHEST SALES")
def find_highest(values):
    return max(values)
daily_sales = [450, 620, 390, 810, 570]
print("Highest sales value:", find_highest(daily_sales))
