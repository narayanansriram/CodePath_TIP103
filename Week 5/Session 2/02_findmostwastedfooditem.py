# You are given a dictionary where the keys are food items and the values are lists of integers representing the amounts of each food item wasted (in grams). Your task is to identify which food item was wasted the most frequently in total.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def find_most_wasted_food_item(waste_records):
  currMax = ("",0)
  for item,waste in waste_records.items():
    totalWaste = sum(waste)
    if totalWaste>currMax[1]:
      currMax = (item,totalWaste)
  return currMax[0]

# Example Usage:

waste_records1 = {
    "Apples": [200, 150, 50],
    "Bananas": [100, 200, 50],
    "Carrots": [150, 100, 200],
    "Tomatoes": [50, 50, 50]
}

result = find_most_wasted_food_item(waste_records1)
print(result) 

waste_records2 = {
    "Bread": [300, 400],
    "Milk": [200, 150],
    "Cheese": [100, 200, 100],
    "Fruits": [400, 100]
}

result = find_most_wasted_food_item(waste_records2)
print(result) 

# Example Output:

# Carrots
# Bread
