# You are tasked with managing food waste records using a queue to simulate the process of handling waste reduction over time. Each record contains a date (in the format "YYYY-MM-DD") and the amount of food wasted on that date. You will process these records using a queue to manage the waste reduction. Return True if the total waste in the queue decreases over time as records are processed and False otherwise.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
from collections import deque
def manage_food_waste_with_queue(waste_records):
  w = deque(waste_records)
  f = None
  s = None
  while w:
    if not f:
      f = w.popleft()[1]
    s = w.popleft()[1]
    if f<s:
      return False
    f = s
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
    ("2024-08-03", 160),
    ("2024-08-04", 140),
    ("2024-08-05", 120)
]

print(manage_food_waste_with_queue(waste_records_1)) 
print(manage_food_waste_with_queue(waste_records_2))

# Example Output:

# True
# False
