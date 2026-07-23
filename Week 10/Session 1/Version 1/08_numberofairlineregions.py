# CodePath Airlines operates in different regions around the world. Some airports are connected directly with flights, while others are not. However, if airport a is connected directly to airport b, and airport b is connected directly to airport c, then airport a is indirectly connected to airport c.

# An airline region is a group of directly or indirectly connected airports and no other airports outside of the group.

# You are given an n x n matrix is_connected where is_connected[i][j] = 1 if CodePath Airlines offers a direct flight between airport i and airport j, and is_connected[i][j] = 0 otherwise.

# Return the total number of airline regions operated by CodePath Airlines.

def num_airline_regions(is_connected):
    adj_list = {}
    n = [i for i in range(len(is_connected))]
    for idx,arr in enumerate(is_connected):
        for jdx,val in enumerate(arr):
            if val == 1:
                # print(idx,jdx)
                if idx not in adj_list:
                    adj_list[idx] = [jdx]
                else:
                    adj_list[idx].append(jdx)
    visited = set()
    def dfs(curr):
        if curr in visited:
            return
        visited.add(curr)
        for neighbor in adj_list[curr]:
            dfs(neighbor)
    count = 0
    for i in range(len(n)):
        if i not in visited:
            count+=1
            dfs(i)
    return count
        

# Example Usage:

is_connected1 = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]

is_connected2 = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [1, 0, 0, 1]
]

print(num_airline_regions(is_connected1))
print(num_airline_regions(is_connected2)) 

# Example Output:

# 2
# 2
