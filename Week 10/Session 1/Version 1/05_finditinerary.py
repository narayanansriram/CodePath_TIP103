# You are a traveler about to embark on a multi-leg journey with multiple flights to arrive at your final travel destination. You have all your boarding passes, but their order has gotten all messed up! You want to organize your boarding passes in the order you will use them, from your first flight all the way to your last flight that will bring you to your final destination.

# Given a list of edges boarding_passes where each element boarding_passes[i] = (departure_airport, arrival_airport) represents a flight from departure_airport to arrival_airport, return an array with the itinerary listing out the airports you will pass through in the order you will visit them. Assume that departure is scheduled from every airport except the final destination, and each airport is visited only once (i.e., there are no cycles in the route).

from collections import defaultdict, deque
def find_itinerary(boarding_passes):
    s = set([i[0] for i in boarding_passes])
    d = set([i[1] for i in boarding_passes])
    source = None
    for i in s:
        if i not in d:
            source = i
    adj_list = defaultdict(str)
    for s,d in boarding_passes:
        adj_list[s] = d
    q = deque()
    q.append(source)
    result = []
    while q:
        curr = q.popleft()
        result.append(curr)
        if curr in adj_list:
            q.append(adj_list[curr])
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
