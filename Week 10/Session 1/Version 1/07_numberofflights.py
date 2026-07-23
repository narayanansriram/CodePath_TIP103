# You are a travel planner and have an adjacency matrix flights with n airports labeled 0 to n-1 where flights[i][j] indicates CodePath Airlines offers a flight from airport i to airport j. You are planning a trip for a client and want to know the minimum number of flights (edges) it will take to travel from airport start to their final destination airport destination on CodePath Airlines.

# Return the minimum number of flights needed to travel from airport i to airport j. If it is not possible to fly from airport i to airport j, return -1.

from collections import defaultdict, deque
def counting_flights(flights, i, j):
    adj_list = defaultdict(set)
    for idx, flight in enumerate(flights):
        for jdx,val in enumerate(flight):
            if val == 1:
                adj_list[idx].add(jdx)
    q = deque()
    q.append(i)
    count = -1
    visited = set()
    while q:
        curr = q.popleft()
        if curr in visited:
            continue
        visited.add(curr)
        if curr == j:
            return count
        count+=1
        if curr in adj_list:
            for neighbor in adj_list[curr]:
                q.append(neighbor)
    return count if curr == j else -1


        


# Example Usage:


# Example usage
flights = [
    [0, 1, 1, 0, 0], # Airport 0
    [0, 0, 1, 0, 0], # Airport 1
    [0, 0, 0, 1, 0], # Airport 2
    [0, 0, 0, 0, 1], # Airport 3
    [0, 0, 0, 0, 0]  # Airport 4
]

print(counting_flights(flights, 0, 2))  
print(counting_flights(flights, 0, 4))
print(counting_flights(flights, 4, 0))

# Example Output:

# 1 
# Example 1 Explanation: Flight path: 0 -> 2
# 3
# Example 2 Explanation: Flight path 0 -> 2 -> 3 -> 4
# -1
# Explanation: Cannot fly from Airport 4 to Airport 0
