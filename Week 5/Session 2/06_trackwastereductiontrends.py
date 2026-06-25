# You are given a sorted list of daily food waste records where each record is a tuple containing a date (in the format "YYYY-MM-DD") and an integer representing the amount of food wasted on that date. Your task is to determine if there is a trend of reducing food waste over time. Return True if each subsequent day shows a decrease in the amount of food wasted compared to the previous day, and False otherwise.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def track_waste_reduction_trends(waste_records):
  i = 0
  j = i+1
  while j<len(waste_records):
    first = waste_records[i][1]
    second = waste_records[j][1]
    if first<second:
      return False
    i+=1
    j+=1
  return True

# Example Usage:

waste_records_1 = [
    ("2024-08-01", 150),
    ("2024-08-02", 120),
    ("2024-08-03", 100),
    ("2024-08-04", 80),
    ("2024-08-05", 60)
]

waste_records_2 = [
    ("2024-08-01", 150),
    ("2024-08-02", 180),
    ("2024-08-03", 150),
    ("2024-08-04", 140),
    ("2024-08-05", 120)
]

print(track_waste_reduction_trends(waste_records_1))
print(track_waste_reduction_trends(waste_records_2))

# Example Output:

# True
# False
