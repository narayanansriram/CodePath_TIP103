from collections import defaultdict

def find_duplicate_chests(chests):
    d = defaultdict(int)
    arr = []
    for c in chests:
        d[c]+=1
        if d[c]>1:
            arr.append(c)
    return arr


# Example Usage:

chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))

# Example Output:

# [2, 3]
# [1]
# []
