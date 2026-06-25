def group_animals_by_habitat(habitats):
    latest_position = {c:i for i,c in enumerate(habitats)}
    ptr = 0
    count = 0
    indices = [-1]
    while ptr<len(habitats):
        curr = habitats[ptr]
        high = latest_position[curr]
        locMax = high
        for j in range(ptr+1,high):
            curr = habitats[j]
            locMax = max(locMax,latest_position[curr])
        # print(ptr)
        indices.append(locMax)
        ptr = locMax+1
    # print(indices,)
# Example Usage:
    indices.append(len(habitats)-1)
    result = []
    for i in range(1,len(indices)):
        result.append(indices[i]-indices[i-1])
    result.pop()
    return result


print(group_animals_by_habitat("ababcbacadefegdehijhklij")) 
print(group_animals_by_habitat("eccbbbbdec"))

# Example Output:

# [9,7,8]
# [10]
