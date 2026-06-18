def min_changes_to_make_balanced(schedule):
    stack = []
    steps = 0
    for i in schedule:
        if i == ")":
            if stack:
                stack.pop()
            else:
                steps+=1
        else:
            stack.append(")")
    while stack:
        steps+=1
        stack.pop()
    return steps
        

# Example Usage:

print(min_changes_to_make_balanced("())"))
print(min_changes_to_make_balanced("(((")) 

# Example Output:

# 1
# 3
