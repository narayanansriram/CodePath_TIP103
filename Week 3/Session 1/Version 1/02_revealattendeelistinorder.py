from collections import deque
def reveal_attendee_list_in_order(attendees):
    attendees.sort()
    q = deque(range(len(attendees)))
    idx_order = []
    while q:
        idx_order.append(q.popleft())
        if q:
            q.append(q.popleft())
    lookup = {idx:num for idx,num in zip(idx_order,attendees) }
    result = []
    for i in range(len(attendees)):
        result.append(lookup[i])
    return result



# Example Usage:

print(reveal_attendee_list_in_order([17,13,11,2,3,5,7])) 
print(reveal_attendee_list_in_order([1,1000]))  

# Example Output:

# [2,13,3,11,5,17,7]
# [1,1000]
test_cases = [
    ([17, 13, 11, 2, 3, 5, 7], [2, 13, 3, 11, 5, 17, 7]),
    ([1, 1000], [1, 1000]),
    ([5], [5]),
    ([4, 2], [2, 4]),
    ([3, 1, 2], [1, 3, 2]),
    ([10, 20, 30, 40], [10, 30, 20, 40]),
    ([9, 8, 7, 6, 5], [5, 7, 6, 9, 8]),
    ([1, 2, 3, 4, 5, 6], [1, 3, 5, 2, 6, 4]),
    ([100, 90, 80, 70, 60, 50, 40, 30], [30, 60, 80, 100, 40, 90, 50, 70]),
    ([6, 1, 5, 2, 4, 3, 7, 8, 9, 10], [1, 5, 2, 6, 3, 8, 4, 10, 7, 9]),
]

for attendees, expected in test_cases:
    print(f"test case {attendees} should be {expected}->{reveal_attendee_list_in_order(attendees)}")