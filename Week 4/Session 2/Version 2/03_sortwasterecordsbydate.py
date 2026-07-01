

# You are given a list of tuples where each tuple contains a date (as a string in the format "YYYY-MM-DD") and a list of integers representing the amount of food wasted on that date. Your task is to sort this list by date in ascending order and return the sorted list.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def sort_waste_records_by_date(waste_records):
  waste_records.sort()
  return waste_records

# Example Usage:

waste_records1 = [
    ("2024-08-15", [300, 200]),
    ("2024-08-13", [150, 100]),
    ("2024-08-14", [200, 250]),
    ("2024-08-12", [100, 50])
]

result = sort_waste_records_by_date(waste_records1)
print(result)

waste_records2 = [
    ("2024-07-05", [400, 150]),
    ("2024-07-01", [200, 300]),
    ("2024-07-03", [100, 100]),
    ("2024-07-04", [50, 50])
]

result = sort_waste_records_by_date(waste_records2)
print(result)

# Example Output:

# [('2024-08-12', [100, 50]), ('2024-08-13', [150, 100]), ('2024-08-14', [200, 250]), ('2024-08-15', [300, 200])]
# [('2024-07-01', [200, 300]), ('2024-07-03', [100, 100]), ('2024-07-04', [50, 50]), ('2024-07-05', [400, 150])]
