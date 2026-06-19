from collections import deque
def blueprint_approval(blueprints):
    stack = []
    for idx,blueprint in enumerate(blueprints):
        # if not stack:
        #     # print(idx,blueprint,"hit if not")
        #     stack.append(blueprint)
        #     continue
        if stack and stack[-1]>blueprint:
            # print(idx,blueprint,"hit if stack and stack-1")
            temp = []
            while stack and stack[-1]>blueprint:
                temp.append(stack.pop())
            stack.append(blueprint)
            while temp:
                stack.append(temp.pop())
        else:
            stack.append(blueprint)
    print(stack)

# Example Usage:

print(blueprint_approval([3, 5, 2, 1, 4])) 
print(blueprint_approval([7, 4, 6, 2, 5])) 

# Example Output:

# [1, 2, 3, 4, 5]
# [2, 4, 5, 6, 7]
