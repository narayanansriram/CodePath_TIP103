def make_balanced_room(s):
    arr = [i for i in s]
    stk = []
    remov = []
    for idx,curr in enumerate(s):
        if curr=="(":
            stk.append(idx)
        elif curr==")":
            if stk:
                stk.pop()
            else:
                remov.append(idx)
    result = []
    for idx,curr in enumerate(s):
        if idx in remov or idx in stk:
            continue
        result.append(curr)
    return "".join(result)
            

# Example Usage:

print(make_balanced_room("art(t(d)e)sign)")) 
print(make_balanced_room("d)e(s)ign")) 
print(make_balanced_room("))((")) 

# Example Output:

# art(t(d)e)sign
# # Note: other outputs such as "art(t(d)esign)" would also be considered balanced and valid
# de(s)ign
