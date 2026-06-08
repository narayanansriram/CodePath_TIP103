def smaller_than_current(nums):
	result = []
	for idx,num in enumerate(nums):
		count = 0
		for j in range(idx):
			if j==idx:
				continue
			if nums[j]<nums[idx]:
				count+=1
		for j in range(idx+1,len(nums)):
			if j==idx:
				continue
			if nums[j]<nums[idx]:
				count+=1
		result.append(count)
	return result
				

# Example Usage:

nums = [8, 1, 2, 2, 3]
print(smaller_than_current(nums))

nums = [6, 5, 4, 8]
print(smaller_than_current(nums))

nums = [7, 7, 7, 7]
print(smaller_than_current(nums))

# Example Output:

# [4, 0, 1, 1, 3]
# [2, 1, 0, 3]
# [0, 0, 0, 0]
