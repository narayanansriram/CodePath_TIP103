# You are given a flight network represented as a directed acyclic graph (DAG) with n airports, labeled from 0 to n - 1. Your goal is to find all possible flight paths from airport 0 (the starting point) to airport n - 1 (the final destination) and return them in any order.

# The flight network is given as follows: flight_routes[i] is a list of all airports you can fly to directly from airport i (i.e., there is a one-way flight from airport i to airport flight_routes[i][j]).

# Write a function that returns all possible flight paths from airport 0 to airport n - 1.

def find_all_flight_routes(flight_routes):
    paths = []
    visited = set()
    def backtrack(node,path):
        if len(flight_routes[node])<1:
            paths.append(path.copy())
            return
        for nei in flight_routes[node]:
            path.append(nei)
            backtrack(nei,path)
            path.pop()
    backtrack(0,[0])
    print(visited)
    return paths


# Example Usage 1:

# 'flight_routes_2' graph diagram

flight_routes_1 = [[1, 2], [3], [3], []]

print(find_all_flight_routes(flight_routes_1))

# Example Output 1:

# [[0, 1, 3], [0, 2, 3]]
# Explanation: 
# - There are two possible paths from airport 0 to airport 3.
# - The first path is: 0 -> 1 -> 3
# - The second path is: 0 -> 2 -> 3

# Example Usage 2:

# 'flight_routes_2' graph diagram

flight_routes_2 = [[4,3,1],[3,2,4],[3],[4],[]]

print(find_all_flight_routes(flight_routes_2))

# Example Output 2:

# [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
