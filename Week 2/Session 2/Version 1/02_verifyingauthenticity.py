from collections import Counter
def is_authentic_collection(art_pieces):
    n = len(art_pieces)-1
    art_tracker = Counter(art_pieces)
    for i in range(1,n+1):
        # print(i, art_tracker)
        if i not in art_tracker:
            return False
        if i==n and art_tracker[i]!=2:
            return False
    return True
# Example Usage:

collection1 = [2, 1, 3]
collection2 = [1, 3, 3, 2]
collection3 = [1, 1]

print(is_authentic_collection(collection1))
print(is_authentic_collection(collection2))
print(is_authentic_collection(collection3))

# Example Output:

# False
# Example 1 Explanation: Since the maximum element of the array is 3, the only 
# candidate n for which this array could be a permutation of base[n], is n = 3. 
# However, base[3] has four elements but array collection1 has three. Therefore, 
# it can not be a permutation of base[3] = [1, 2, 3, 3]. So the answer is false.

# True
# Example 2 Explanation:  Since the maximum element of the array is 3, the only 
# candidate n for which this array could be a permutation of base[n], is n = 3. 
# It can be seen that collection2 is a permutation of base[3] = [1, 2, 3, 3] 
# (by swapping the second and fourth elements in nums, we reach base[3]).
#  Therefore, the answer is true.

# True
# Example 3 Explanation; Since the maximum element of the array is 1, 
# the only candidate n for which this array could be a permutation of base[n], 
# is n = 1. It can be seen that collection3 is a permutation of base[1] = [1, 1].
#  Therefore, the answer is true.
