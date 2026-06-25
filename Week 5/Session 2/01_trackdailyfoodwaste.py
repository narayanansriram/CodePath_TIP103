# You are given a dictionary where the keys are dates in the format "YYYY-MM-DD" and the values are lists of integers representing the amounts of food waste (in grams) recorded on that date. Your task is to calculate the total amount of food waste for each day and return the dates and the total waste amounts for those dates.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def track_daily_food_waste(waste_records):
  result = {}
  for timestamp,waste in waste_records.items():
    result[timestamp] = sum(waste)
  return result

# Example Usage:

waste_records1 = {
    "2024-08-01": [200, 150, 50],
    "2024-08-02": [300, 400],
    "2024-08-03": [100]
}

result = track_daily_food_waste(waste_records1)
print(result)

waste_records2 = {
    "2024-07-01": [120, 80],
    "2024-07-02": [150, 200, 50],
    "2024-07-03": [300, 100]
}

result = track_daily_food_waste(waste_records2)
print(result)

# Example Output:

# {'2024-08-01': 400, '2024-08-02': 700, '2024-08-03': 100}
# {'2024-07-01': 200, '2024-07-02': 400, '2024-07-03': 400}
