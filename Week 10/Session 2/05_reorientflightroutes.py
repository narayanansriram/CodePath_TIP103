# There are n airports numbered from 0 to n - 1 and n - 1 direct flight routes between airports such that there is exactly one way to travel between any two airports (this network forms a tree). Last year, the aviation authority decided to orient the flight routes in one direction due to air traffic regulations.

# Flight routes are represented by connections, where connections[i] = [airport_a, airport_b] represents a one-way flight route from airport airport_a to airport airport_b.

# This year, there will be a major aviation event at the central hub (airport 0), and many flights need to reach this hub.

# Your task is to reorient some flight routes so that every airport can send flights to airport 0. Return the minimum number of flight routes that need to be reoriented.

# It is guaranteed that after the reordering, each airport will be able to send a flight to airport 0.

from collections import deque

def min_reorient_flight_routes(n, connections):
    q = deque()
    d = {}
    for c1,c2 in connections:
        d[c1]=c2
    # path = []
    visited = set()
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        if node not in d:
            return
        nei = d[node]
        if nei not in visited:
            dfs(nei)
    count = 0
    for i in range(n):
        if i not in visited:
            dfs(i)
            count+=1
    return count
# Example Usage:

n = 6
connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]

print(min_reorient_flight_routes(n, connections))

# Example Output:

# 3
# Explanation: 
# - Initially, the flight routes are: 0 -> 1, 1 -> 3, 2 -> 3, 4 -> 0, 4 -> 5
# - We need to reorient the routes [1, 3], [2, 3], and [4, 5] to ensure that every airport can send a flight to airport 0.
