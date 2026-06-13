from collections import Counter
def min_steps_to_match_maps(map1, map2):
    m1 = Counter(map1)
    for c in map2:
        if c in m1:
            m1[c]-=1
        else:
            m1[c]=-1
    steps = 0
    for v in m1.values():
        if v<0:
            steps-=v

    return steps

# Example Usage:

map1_1 = "bab"
map2_1 = "aba"
map1_2 = "treasure"
map2_2 = "huntgold"
map1_3 = "anagram"
map2_3 = "mangaar"

print(min_steps_to_match_maps(map1_1, map2_1))
print(min_steps_to_match_maps(map1_2, map2_2))
print(min_steps_to_match_maps(map1_3, map2_3))

# Example Output:

# 1
# 6
# 0
