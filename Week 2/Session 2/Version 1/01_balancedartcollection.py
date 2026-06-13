from collections import Counter
def find_balanced_subsequence(art_pieces):
    d = Counter(art_pieces)
    maxSize = 0
    for k,v in d.items():
        if k+1 in d:
            maxSize = max(maxSize, v+d[k+1])
    return maxSize


# Example Usage:

art_pieces1 = [1,3,2,2,5,2,3,7]
art_pieces2 = [1,2,3,4]
art_pieces3 = [1,1,1,1]

print(find_balanced_subsequence(art_pieces1))
print(find_balanced_subsequence(art_pieces2))
print(find_balanced_subsequence(art_pieces3))

# Example Output:

# 5
# Example 1 Explanation:  The longest balanced subsequence is [3,2,2,2,3].

# 2
# 0
