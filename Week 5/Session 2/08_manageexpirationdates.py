# Simulate managing food items in a pantry by using a stack to keep track of their expiration dates. Determine if the items are ordered correctly by expiration date (the first item to expire should be at the top of the stack). Return True if items are ordered correctly and False otherwise.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def check_expiration_order(expiration_dates):
  stk = []
  for item,expiration_date in expiration_dates:
    if stk and stk[-1]>expiration_date:
      return False
    else:
      stk.append(expiration_date)
  return True

# Example Usage:

expiration_dates_1 = [
    ("Milk", "2024-08-05"),
    ("Bread", "2024-08-10"),
    ("Eggs", "2024-08-12"),
    ("Cheese", "2024-08-15")
]

expiration_dates_2 = [
    ("Cheese", "2024-08-15"),
    ("Bread", "2024-08-12"),
    ("Eggs", "2024-08-10"),
    ("Milk", "2024-08-05")
]

print(check_expiration_order(expiration_dates_1)) 
print(check_expiration_order(expiration_dates_2)) 

# Example Output:

# True
# False
