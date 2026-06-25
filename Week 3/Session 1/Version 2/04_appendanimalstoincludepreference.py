def append_animals(available, preferred):
  p,a = 0,0
  while p<len(preferred) and a<len(available):
    if preferred[p]==available[a]:
      p+=1
    a+=1
  return len(preferred)-p

# Example Usage:

print(append_animals("catsdogs", "cows")) 
print(append_animals("rabbit", "r")) 
print(append_animals("fish", "bird"))

# Example Output:

# 2
# 0
# 4
