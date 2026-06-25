def rearrange_animal_names(s):
  output = ""
  stk = []
  word = ""
  for c in s:
      if c == ")":
        while stk and stk[-1]!=")":
            word+=(stk.pop())
        stk.pop()
        stk.append(word)
        word = ""
      elif c == "(":
         stk.append(")")
      else:
         word+=c
      print(stk,word)
  while stk:
     output+=stk.pop()
  return output



# Example Usage:

# print(rearrange_animal_names("(dribtacgod)"))
print(rearrange_animal_names("(!(love(stac))I)")) 
# print(rearrange_animal_names("adopt(yadot(a(tep)))!")) 

# Example Output:

# dogcatbird
# Ilovecats!
# adoptapettoday!
