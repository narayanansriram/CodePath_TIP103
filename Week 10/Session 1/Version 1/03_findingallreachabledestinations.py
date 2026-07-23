# You are a travel coordinator for CodePath Airlines, and you're helping a customer find all possible destinations they can reach from a starting airport. The flight connections between airports are represented as an adjacency dictionary flights, where each key is a destination, and the corresponding value is a list of other destinations that are reachable through a direct flight.

# Given a starting location start, return a list of all destinations reachable from the start location either through a direct flight or connecting flights with layovers. The list should be provided in ascending order by number of layovers required.

from collections import deque
def get_all_destinations(flights, start):
    q = deque()
    q.append(start)
    visited = []

    while q:
        curr = q.popleft()
        if curr in visited:
            continue
        visited.append(curr)
        for s in flights[curr]:
            q.append(s)
    return visited


# Example Usage:

# 'flights' graph diagram

flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"],
    "New York": ["Helsinki", "Reykjavik"]   
}

print(get_all_destinations(flights, "Beijing"))
print(get_all_destinations(flights, "Helsinki"))

# Example Output:

['Beijing', 'Mexico City', 'Helsinki', 'Sydney', 'Cairo', 'New York', 'Tokyo', 
'Reykjavik']
['Helsinki', 'Cairo', 'New York', 'Reykjavik']
