# You are given an adjacency dictionary flights where for any location source, flights[source] is a list of tuples in the form (destination, cost) indicating that there exists a flight from source to destination at ticket price cost.

# Given a starting location start and a final destination dest return the total cost of flying from start to dest. If it is not possible to fly from start to dest, return -1. If there are multiple possible paths from start to dest, return any of the possible answers.
from collections import deque
def calculate_cost(flights, start, dest):
    q = deque()
    q.append((start,0))
    visited = set()
    while q:
        curr, score = q.popleft()
        if curr in visited:
            continue
        if curr == dest:
            return score
        for nextStop, nextScore in flights[curr]:
            q.append((nextStop,nextScore+score))

# Example Usage:

flights = {
    'LAX': [('SFO', 50)],
    'SFO': [('LAX', 50), ('ORD', 100), ('ERW', 210)],
    'ERW': [('SFO', 210), ('ORD', 300)],
    'ORD': [('ERW', 300), ('SFO', 100), ('MIA', 400)],
    'MIA': [('ORD', 400)]
}

print(calculate_cost(flights, 'LAX', 'MIA'))

# Example Output:

# 550
# Explanation: There is a path from LAX -> SFO -> ORD -> MIA with ticket prices 50 + 100 + 400 = 550
# 960 would also be an acceptable answer following the path from LAX -> SFO -> ERW -> ORD -> MIA
