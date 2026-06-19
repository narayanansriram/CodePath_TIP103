def next_greater_dream(dreams):
    bigdreams = dreams+dreams
    # print(bigdreams)
    result = [0]*len(bigdreams)
    stk = []
    for idx,dream in enumerate(bigdreams):
        if stk and bigdreams[stk[-1]]<dream:
            while stk and bigdreams[stk[-1]]<dream:
                prev = stk.pop()
                result[prev]=dream
            stk.append(idx)
        else:
            stk.append(idx)
    while stk:
        prev = stk.pop()
        result[prev]=-1
    # print(result[:len(dreams)])
    return result[:len(dreams)]
# Example Usage:

print(next_greater_dream([1, 2, 1])) 
print(next_greater_dream([1, 2, 3, 4, 3])) 

# Example Output:

# [2, -1, 2]
# [2, 3, 4, -1, 4]
