from collections import Counter
def beauty_sum(collection):
    c = Counter(collection)
    bCount = max(c.values())-min(c.values())
    for i in range(3,len(collection)):
        for j in range(len(collection)-i+1):
            # print(collection[j:j+i],i)
            c = Counter(collection[j:j+i])
            if len(c)>0:
                # print(c,collection[j:j+1])
                bCount += max(c.values())-min(c.values())
            
    return bCount




# Example Usage:

print(beauty_sum("aabcb")) 
print(beauty_sum("aabcbaa"))

# Example Output:

# 5
# Example 1 Explanation: The substrings with non-zero beauty are 
# ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.

# 17
