# If you implemented find_itinerary() in the previous problem without using Depth First Search, solve it using DFS. If you solved it using DFS, try solving it using an alternative approach.

from collections import defaultdict
def find_itinerary(boarding_passes):
    s = set([i[0] for i in boarding_passes])
    d = set([i[1] for i in boarding_passes])
    source = None
    for i in s:
        if i not in d:
            source = i
            break
    adj_list = defaultdict(str)
    for s,d in boarding_passes:
        adj_list[s] = d
    stk = [source]
    result = []
    while stk:
        curr = stk.pop()
        if curr in result:
            continue
        result.append(curr)
        if curr in adj_list:
            stk.append(adj_list[curr])
    return result

# Example Usage:

boarding_passes_1 = [
                    ("JFK", "ATL"),
                    ("SFO", "JFK"),
                    ("ATL", "ORD"),
                    ("LAX", "SFO")]

boarding_passes_2 = [
                    ("LAX", "DXB"),
                    ("DFW", "JFK"),
                    ("LHR", "DFW"),
                    ("JFK", "LAX")]

print(find_itinerary(boarding_passes_1))
print(find_itinerary(boarding_passes_2))

# Example Output:

# ['LAX', 'SFO', 'JFK', 'ATL', 'ORD']
# ['LHR', 'DFW', 'JFK', 'LAX', 'DXB']
