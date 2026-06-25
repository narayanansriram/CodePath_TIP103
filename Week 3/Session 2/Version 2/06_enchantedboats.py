import heapq
def num_enchanted_boats(creatures, limit):
  heapq.heapify(creatures)
  count = 1
  curr = 0
  while creatures:
    if creatures[0]+curr<=limit:
      curr+=heapq.heappop(creatures)
    else:
      count+=1
      curr = 0
  return count

# Example Usage:

print(num_enchanted_boats([1, 2], 3)) 
print(num_enchanted_boats([3, 2, 2, 1], 3)) 
print(num_enchanted_boats([3, 5, 3, 4], 5)) 

# Example Output:

# 1
# 3
# 4
