# The Rebel Alliance has intercepted a crucial sequence of encrypted transmissions from the evil Empire. Each transmission is marked with a unique frequency code, represented as integers, and these codes are stored in a sorted array transmissions. As a skilled codebreaker for the Rebellion, write a function find_frequency_positions() that returns a tuple with the first and last indices of a specific frequency code target_code in transmissions. If target_code does not exist in transmissions, return (-1, -1).

# Your solution must have O(log n) time complexity.

def find_frequency_positions(transmissions, target_code):
    ltar = target_code-1
    rtar = target_code+1
    def binarysearch1(arr,target):
        lo,hi = 0,len(arr)-1
        while lo<=hi:
            mid = lo + (hi-lo)//2
            if arr[mid]<target:
                lo = mid+1
            elif arr[mid]>=target:
                hi = mid-1
        return lo if 0<=lo<len(arr) else -1
    def binarysearch2(arr,target):
        lo,hi = 0,len(arr)-1
        while lo<=hi:
            mid = lo + (hi-lo)//2
            if arr[mid]<=target:
                lo = mid+1
            elif arr[mid]>target:
                hi = mid-1
        return lo-1 if 0<=lo-1<len(arr) else -1
    lower = binarysearch1(transmissions,target_code)
    upper = binarysearch2(transmissions,target_code)
    if lower==-1 or lower>upper:
        return [-1,-1]
    return [lower,upper]


# Example Usage:

print(find_frequency_positions([5,7,7,8,8,10], 8))
print(find_frequency_positions([5,7,7,8,8,10], 6))
print(find_frequency_positions([], 0))
print(find_frequency_positions([5,7,7,8,8,10], 5))
print(find_frequency_positions([5,7,7,8,8,10], 11))

# Example Output:

# (3, 4)
# (-1, -1)
# (-1, -1)
