from collections import defaultdict
def organize_pirate_crew(group_sizes):
    lookup = defaultdict(list)
    for idx,group_size in enumerate(group_sizes):
        lookup[group_size].append(idx)
    result = []
    for k,v in lookup.items():
        curr = []
        for i in v:
            curr.append(i)
            if len(curr) == k:
                result.append(curr)
                curr = []
    return result

# Example Usage:

group_sizes1 = [3, 3, 3, 3, 3, 1, 3]
group_sizes2 = [2, 1, 3, 3, 3, 2]

print(organize_pirate_crew(group_sizes1))
print(organize_pirate_crew(group_sizes2)) 

# Example Output:

# [[5], [0, 1, 2], [3, 4, 6]]
# [[1], [0, 5], [2, 3, 4]]
