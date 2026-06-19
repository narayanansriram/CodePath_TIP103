def time_to_complete_dream_designs(design_times):
    stk = []
    result = [0]*len(design_times)
    for idx,design_time in enumerate(design_times):
        # print(stk,idx,design_times)
        if not stk:
            stk.append(idx)
        elif stk and design_times[(stk[-1])]<design_time:
            while stk and design_times[stk[-1]]<design_time:
                prev = stk.pop()
                result[prev] = idx-prev
            stk.append(idx)
        else:
            stk.append(idx)
    return result
# Example Usage:

print(time_to_complete_dream_designs([3, 4, 5, 2, 1, 6, 7, 3])) 
print(time_to_complete_dream_designs([2, 3, 1, 4]))  
print(time_to_complete_dream_designs([5, 5, 5, 5]))  

# Example Output:

# [1, 1, 3, 2, 1, 1, 0, 0]
# [1, 2, 1, 0]
# [0, 0, 0, 0]
