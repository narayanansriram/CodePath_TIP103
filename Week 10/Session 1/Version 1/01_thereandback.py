# As a flight coordinator for CodePath airlines, you have a 0-indexed adjacency list flights with n nodes where each node represents the ID of a different destination and flights[i] is an integer array indicating that there is a flight from destination i to each destination in flights[i]. Write a function bidirectional_flights() that returns True if for every flight from a destination i to a destination j there also exists a flight from destination j to destination i. Return False otherwise.

from collections import defaultdict
def bidirectional_flights(flights):
    adj_list = defaultdict(list)
    candidates = defaultdict(list)
    for f1,f2 in enumerate(flights):
        for i in f2:
            adj_list[f1].append(i)
            candidates[i].append(f1)
    return adj_list == candidates

# Example Usage:

# Example 1: flights1

# 'flights1' graph diagram

# Example 2: flights2 'flights2' graph diagram

flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

print(bidirectional_flights(flights1))
print(bidirectional_flights(flights2))

# Example Output:

# True
# False
