# Given an adjacency dictionary of flights flights where each key is an airport i and flights[i] is an array indicating that there is a flight from destination i to each destination in flights[i], return an array with the flight path from a given source location to a given destination location.

# If there are multiple flight paths from the source to destination, return any flight path.

from collections import deque
def get_itinerary(flights, source, destination):
    stk = []
    stk.append(source)
    visited = set()
    path = []
    while stk:
        curr = stk.pop()
        if curr in visited:
            continue
        visited.add(curr)
        path.append(curr)
        if curr==destination:
            return path
        for nei in flights[curr]:
            stk.append(nei)

# Example Usage:

flights = {
    'LAX': ['SFO'],
    'SFO': ['LAX', 'ORD', 'ERW'],
    'ERW': ['SFO', 'ORD'],
    'ORD': ['ERW', 'SFO', 'MIA'],
    'MIA': ['ORD']
}

print(get_itinerary(flights, 'LAX', 'MIA'))

# Example Output:

# ['LAX', 'SFO', 'ORD', 'MIA']
# Explanation: ['LAX', 'SFO', 'ERW', 'ORD', 'MIA'] is also a valid answer
