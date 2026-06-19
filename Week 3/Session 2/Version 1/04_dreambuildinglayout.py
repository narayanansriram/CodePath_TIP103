def min_swaps(s):
    stk = []
    for i in s:
        if i=="]":
            if stk:
                stk.pop()
        else:
            stk.append("]")
    return len(stk)//2 + len(stk)%2

# Example Usage:

print(min_swaps("][][")) 
print(min_swaps("]]][[[")) 
print(min_swaps("[]"))  

# Example Output:

# 1
# 2
# 0
