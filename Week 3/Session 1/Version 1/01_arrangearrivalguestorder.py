def arrange_guest_arrival_order(arrival_pattern):
    n = len(arrival_pattern)
    slots = [i for i in range(n+1,0,-1)]
    d_stack = []
    queue = []
    for i in range(len(arrival_pattern)):
        if arrival_pattern[i]=="I":
            queue.append(str(slots.pop()))
            while len(d_stack)>0:
                pos = d_stack.pop()
                queue[pos] = str(slots.pop())
        elif arrival_pattern[i]=="D":
            queue.append(" ")
            d_stack.append(i)
    last = slots.pop()
    while len(d_stack)>0:
        pos = d_stack.pop()
        queue[pos]=str(slots.pop())
    while len(slots)>0:
        queue.append(str(slots.pop()))
    queue.append(str(last))
    print(queue)
    return "".join(queue)

# Example Usage:

print(arrange_guest_arrival_order("IIIDIDDD"))  
print(arrange_guest_arrival_order("DDD"))  

# Example Output:

# 123549876
# 4321
test_cases = [
    ("I", "12"),
    ("D", "21"),
    ("II", "123"),
    ("DD", "321"),
    ("ID", "132"),
    ("DI", "213"),
    ("", "1"),
    ("IDIDIDID", "192837465"),
    ("DIDIDIDI", "219384756"),
    ("IIIII", "123456"),
    ("DDDDD", "654321"),
    ("DDIIDD", "3214765"),
    ("IIDDI", "124365"),
    ("IIDII", "1246357"),
    ("IIIDIDDD", "123549876"),
    ("DDD", "4321"),
]

# for pattern, expected in test_cases:
#     print(f"test case {pattern!r} should be {expected} --> got {arrange_guest_arrival_order(pattern)}")

print(arrange_guest_arrival_order("IDID"))  # Output: "13254"
print(arrange_guest_arrival_order("III"))   # Output: "1234"
print(arrange_guest_arrival_order("DDI"))   # Output: "3214"