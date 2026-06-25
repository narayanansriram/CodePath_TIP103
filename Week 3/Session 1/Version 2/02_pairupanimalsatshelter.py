def pair_up_animals(discomfort_levels):
  discomfort_levels.sort()
  pair_sum = 0
  l,r = 0,len(discomfort_levels)-1
  while l<r:
    pair_sum = max(pair_sum,discomfort_levels[l]+discomfort_levels[r])
    l+=1
    r-=1
  return pair_sum

# Example Usage:

print(pair_up_animals([3,5,2,3]))  
print(pair_up_animals([3,5,4,2,4,6])) 

# Example Output:

# 7
# 8
