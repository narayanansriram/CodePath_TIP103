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

        return processed_count =