def hulk_smash(n):
	output = []
	for i in range(1,n+1):
		if i%3==0 and i%5==0:
			output.append("HulkSmash")
		elif i%3==0:
			output.append("Hulk")
		elif i%5==0:
			output.append("Smash")
		else:
			output.append(i)
	return output

# Example Usage:

n = 3
print(hulk_smash(n))

n = 5
print(hulk_smash(n))

n = 15
print(hulk_smash(n))

# Example Output:

# ["1", "2", "Hulk"]
# ["1", "2", "Hulk", "4", "Smash"]
# ["1", "2", "Hulk", "4", "Smash", "Hulk", "7", "8", "Hulk", "Smash", "11", "Hulk", "13", "14", "HulkSmash"]
