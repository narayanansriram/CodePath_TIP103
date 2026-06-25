def token_value(token):
  stk = []
  tokval  = 0
  for t in token:
    # print(t,nest)
    if t==")":
      if stk:
        if stk[-1]==0:
          stk.pop()
          tokval+=1
        else:
           curr = stk.pop()
           stk.append(2*curr)
        
    else:
      stk.append(0)
#   print("-----")
  return tokval

# Example Usage:

print(token_value("()"))
print(token_value("(())")) 
print(token_value("((()))")) 
print(token_value("()()")) 

# Example Output:

# 1
# 2
# 3
# 2
