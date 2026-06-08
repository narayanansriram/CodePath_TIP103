def two_sum(nums, target):
    lo = 0
    hi = len(nums)-1
    while lo<hi:
        curr = nums[lo]+nums[hi]
        print(curr)
        if curr==target:
            return [lo,hi]
        elif curr<target:
            lo+=1
        else:
            hi-=1
    return -1

# Example Usage

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))

nums = [2, 7, 11, 15]
target = 18
print(two_sum(nums, target))

# Example Output:

[0, 1]
[1, 2]
