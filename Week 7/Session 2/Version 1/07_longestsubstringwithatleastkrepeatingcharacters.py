# Given a string s and an integer k, use a divide and conquer approach to return the length of the longest substring of s such that the frequency of each character in substring is greater than or equal to k.

# If no such substring exists, return 0.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

from collections import Counter,defaultdict
def longest_substring(s, k):
    currMax = 0
    def helper(a):
        c = Counter(a)
        if all([v>=k for _,v in c.items()]):
            nonlocal currMax
            currMax = max(currMax,sum(c.values()))
        if len(a)<1:
            return 0
        for i in range(len(a)):
            if c[a[i]]<k:
                helper(a[:i])
                helper(a[i+1:])
    helper(s)
    return currMax
        
        
        


# Example Usage:

print(longest_substring("tatooine", 2))
print(longest_substring("chewbacca", 2))
print(longest_substring("chewbacccccccca", 2))

# Example Output:

# 2
# Example 1 Explanation: The longest substring is 'oo' as 'o' is repeated 2 times.

# 4
# Example 2 Explanation: The longest substirng is 'acca' as both 'a' and 'c' are repeated 2 times.
