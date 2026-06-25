from collections import deque
def validate_shelter_sequence(admitted, adopted):
  adopt_stack = adopted.copy()
  admitted_queue = deque(admitted)
  while adopt_stack:
    curr = adopt_stack.pop()
    if admitted_queue[0]==curr:
      admitted_queue.popleft()
    elif admitted_queue[-1]==curr:
      admitted_queue.pop()
    else:
      return False
  return True

# Example Usage:

print(validate_shelter_sequence([1,2,3,4,5], [4,5,3,2,1]))
print(validate_shelter_sequence([1,2,3,4,5], [4,3,5,1,2])) 

# Example Output:

# True
# False
