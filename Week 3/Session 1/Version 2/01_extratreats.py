from collections import deque
def predictAdoption_victory(votes):
  
  c = deque()
  d = deque()
  for i,a in enumerate(votes):
    if a=="C":
      c.append(i)
    else:
      d.append(i)
  while c and d:
    cPick = c.popleft()
    dPick = d.popleft()
    if cPick<dPick:
      c.append(cPick+len(votes))
    else:
      d.append(dPick+len(votes))
#   print(c,d)
  return "Cat Lovers" if len(c)>0 else "Dog Lovers"


# Example Usage:

print(predictAdoption_victory("CD")) 
print(predictAdoption_victory("CDD")) 
print(predictAdoption_victory("DC"))
print(predictAdoption_victory("DCC"))  

# Example Output:

# Cat Lovers
# Dog Lovers
# Dog Lovers
# Cat Lovers
