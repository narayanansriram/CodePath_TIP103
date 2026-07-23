# You are applying to become a pilot for CodePath Airlines, and you must complete a series of flight training courses. There are a total of num_courses flight courses you have to take, labeled from 0 to num_courses - 1. Some courses have prerequisites that must be completed before you can take the next one.

# You are given an array flight_prerequisites where flight_prerequisites[i] = [a, b] indicates that you must complete course b first in order to take course a.

# For example, the pair ["Advanced Maneuvers", "Basic Navigation"] indicates that to take "Advanced Maneuvers", you must first complete "Basic Navigation".

# Return True if it is possible to complete all flight training courses. Otherwise, return False.

from collections import defaultdict, deque
def can_complete_flight_training(num_courses, flight_prerequisites):
    adj_list = defaultdict(list)
    in_degree = defaultdict(int)   # string-keyed, not a list

    for a, b in flight_prerequisites:
        adj_list[b].append(a)
        in_degree[a] += 1

    # Seed the queue with every course that appears with in_degree 0,
    # including courses that never appear as an "a" at all (no prereqs, never mentioned as needing something)
    all_courses = set()
    for a, b in flight_prerequisites:
        all_courses.add(a)
        all_courses.add(b)

    q = deque()
    for course in all_courses:
        if in_degree[course] == 0:
            q.append(course)

    processed_count = 0
    while q:
        curr = q.popleft()
        processed_count += 1
        for neighbor in adj_list[curr]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                q.append(neighbor)

    return processed_count == num_courses


# Example Usage:

flight_prerequisites_1 = [['Advanced Maneuvers', 'Basic Navigation']]
flight_prerequisites_2 = [['Advanced Maneuvers', 'Basic Navigation'], ['Basic Navigation', 'Advanced Maneuvers']]

print(can_complete_flight_training(2, flight_prerequisites_1))
print(can_complete_flight_training(2, flight_prerequisites_2))

# Example Output:

# True
# Example 1 Explanation: There are 2 flight training courses. To take *Advanced Maneuvers*, you must first complete *Basic Navigation*. This is possible.
# False
# Example 1 Explanation: There are 2 flight training courses. To take *Advanced Maneuvers*, you must first complete *Basic Navigation*, but to take *Basic Navigation*, you must first complete *Advanced Maneuvers*. This creates a cycle, making it impossible to complete all courses.
