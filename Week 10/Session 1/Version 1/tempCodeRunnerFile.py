 adj_list = defaultdict(str)
    for s,d in boarding_passes:
        adj_list[s] = d
    q = deque()
    q.append(source)
    result = []