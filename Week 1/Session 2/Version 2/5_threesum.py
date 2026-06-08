def three_sum(nums):
    results = set()
    nums.sort()
    for i in range(len(nums)):
        # print(nums)
        if nums[i]>0:
            break
        j = i+1
        k = len(nums)-1
        while j<k:
            curr = nums[i]+nums[j]+nums[k]
            # print(i,j,k,nums[i],nums[j],nums[k],curr)
            if curr == 0:
                results.add((nums[i],nums[j],nums[k]))
                j+=1
            elif curr>0:
                k-=1
            else:
                j+=1
    return list(results)

# Example Usage

nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))

nums = [0, 1, 1]
print(three_sum(nums))

nums = [0, 0, 0]
print(three_sum(nums))

# Example Output:

# [[-1, -1, 2], [-1, 0, 1]]
# []
# [[0, 0, 0]]
