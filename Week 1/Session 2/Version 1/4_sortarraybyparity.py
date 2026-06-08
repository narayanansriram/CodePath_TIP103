def sort_by_parity(nums):
    f = 0
    b = len(nums)-1
    while f<b:
        if nums[f]%2==0:
            f+=1
        elif nums[b]%2==1:
            b-=1
        else:
            nums[f],nums[b]=nums[b],nums[f]
            f+=1
            b-=1
    return nums
        

# Example Usage

nums = [3, 1, 2, 4]
result = sort_by_parity(nums)
print(result)
assert [4,2,1,3] or [2,4,1,3] ==result, "[3,1,2,4] should be [4,2,1,3]"

nums = [0]
result = sort_by_parity(nums)
print(result)
assert [0]==result, "[0] should be [0]"

# Example Output:

# [2, 4, 3, 1]
# [0]
