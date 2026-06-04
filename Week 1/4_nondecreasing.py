def non_decreasing(nums):
	change = 0
	for i in range(1,len(nums)):
		if nums[i]<=nums[i-1]:
			change+=1
		if change>1:
			return False
	return True

# Example Usage:

nums = [4, 2, 3]
print(non_decreasing(nums))
assert True == non_decreasing(nums), "Check that [4,2,3] is non decreasing which it is since 4=1@index 0"

nums = [4, 2, 1]
print(non_decreasing(nums))
assert False == non_decreasing(nums), "Check that [4,2,1] is NOT non decreasing which it is since 2 indices have to be changed"

# Example Output:

# True
# False
