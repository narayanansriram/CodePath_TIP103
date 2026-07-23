from collections import defaultdict, deque

def topological_sort_blueprint(num_nodes, edges):
    # ---- 1. Build the graph AND in-degree count ----
    adj_list = defaultdict(list)   # node -> list of nodes it points TO (unlocks)
    in_degree = [0] * num_nodes     # how many prerequisites/incoming edges each node has

    for a, b in edges:
        # if edge means "b must come before a" (b is a prerequisite of a):
        adj_list[b].append(a)       # completing b unlocks a
        in_degree[a] += 1           # a now has one more prerequisite

    # ---- 2. Seed the queue with every node that has NO prerequisites ----
    q = deque()
    for node in range(num_nodes):
        if in_degree[node] == 0:
            q.append(node)

    # ---- 3. Process nodes in "unlocked" order ----
    order = []          # optional: the actual topological order, if you need it
    processed_count = 0

    while q:
        curr = q.popleft()
        order.append(curr)
        processed_count += 1

        for neighbor in adj_list[curr]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                q.append(neighbor)

    # ---- 4. Check for a cycle ----
    if processed_count != num_nodes:
        return False   # or: return [] / raise, depending on what the problem wants
    return True         # or: return order, if the problem wants the actual sequence