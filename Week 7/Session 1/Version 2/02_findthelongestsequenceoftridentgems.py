# The people of Atlantis are collecting rare Trident Gems as they explore the ocean. The gems are arranged in a sequence of integers representing their value. Write a recursive function that returns the length of the consecutive sequence of gems where each subsequent value increases by exactly 1.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def longest_trident_sequence(gems):
    currMax = 0
    def sequencer(num,idx):
        nonlocal currMax
        if idx>=len(gems):
            return 1
        if gems[idx]==(num+1):
            x = sequencer(gems[idx],idx+1)
            # print(f"if-->{x},{num},{arr}")
            currMax = max(currMax,1+x)
            return 1 + x
        else:
            sequencer(gems[idx],idx+1)
            # print(f"else")
            # return 1
        return 0
    sequencer(gems[0],1)
    return currMax

# Example Usage:

print(longest_trident_sequence([1, 2, 3, 2, 3, 4, 5, 6]))
print(longest_trident_sequence([5, 10, 7, 8, 1, 2]))
print(longest_trident_sequence([1, 2, 3, 4, 5, 6,7,8,9]))

# Example Output:

# 5
# Example 1 Explanation: longest sequence is 2, 3, 4, 5, 6

# 2
# Example 2 Explanation: longest sequence is 7, 8 or 1, 2
