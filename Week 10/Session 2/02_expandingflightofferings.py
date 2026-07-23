# CodePath Airlines wants to expand their flight offerings so that for any airport they operate out of, it is possible to reach all other airports. They track their current flight offerings in an adjacency dictionary flights where each key is an airport i and flights[i] is an array indicating that there is a flight from destination i to each destination in flights[i]. Assume that if there is flight from airport i to airport j, the reverse is also true.

# Given flights, return the minimum number of flights (edges) that need to be added such that there is flight path from each airport in flights to every other airport.

def min_flights_to_expand(flights):
    src_list = set(flights.keys())
    for v in flights.values():
        for e in v:
            src_list.add(e)
    visited = set()
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for nei in flights[node]:
            dfs(nei)
    count=0
    for s in src_list:
        if s not in visited:
            count+=1
            dfs(s)
    return count-1



# Example Usage:

flights = {
    'JFK': ['LAX', 'SFO'],
    'LAX': ['JFK', 'SFO'],
    'SFO': ['JFK', 'LAX'],
    'ORD': ['ATL'],
    'ATL': ['ORD']
}

print(min_flights_to_expand(flights))

# Example Output:

# 1
