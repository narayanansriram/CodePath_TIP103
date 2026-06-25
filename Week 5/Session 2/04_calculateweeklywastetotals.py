# You have a dictionary where each key represents a day of the week, and the value for each key is a list of integers representing the amount of food waste (in kilograms) recorded for that day. Your task is to calculate the total food waste for each week and return the results as a dictionary where the keys are the days of the week and the values are the total food waste for each day.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def calculate_weekly_waste_totals(weekly_waste):
  d = {}
  for day,waste in weekly_waste.items():
    d[day]=sum(waste)
  return d

# Example Usage:

weekly_waste = {
    'Monday': [5, 3, 7],
    'Tuesday': [2, 4, 6],
    'Wednesday': [8, 1],
    'Thursday': [4, 5],
    'Friday': [3, 2, 1],
    'Saturday': [6],
    'Sunday': [1, 2, 2]
}
print(calculate_weekly_waste_totals(weekly_waste))

# Example Output:

# {'Monday': 15, 'Tuesday': 12, 'Wednesday': 9, 'Thursday': 9, 'Friday': 6, 'Saturday': 6, 'Sunday': 5}
