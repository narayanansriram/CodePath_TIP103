def count_divisible_collections(collection_sizes, k):
    count = 0
    for i in range(len(collection_sizes)):
        for j in range(len(collection_sizes)-i+1):
            # print(collection_sizes[i:i+j])
            if len(collection_sizes[i:i+j])>0 and sum(collection_sizes[i:i+j])%k == 0:
                count+=1
    return count

# Example Usage:

nums1 = [4, 5, 0, -2, -3, 1]
k1 = 5
nums2 = [5]
k2 = 9

print(count_divisible_collections(nums1, k1))  
print(count_divisible_collections(nums2, k2))  

# Example Output:

# 7
# Example 1 Explanation: There are 7 subarrays with a sum divisible by k = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

# 0
