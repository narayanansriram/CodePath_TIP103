def find_missing_clues(clues, lower, upper):
	result = []
	if (clues[0]-lower)>1:
		result.append([lower,clues[0]-1])
	for i in range(1,len(clues)):
		if (clues[i]-clues[i-1])>1:
			result.append([clues[i-1]+1,clues[i]-1])
	if (upper-clues[-1])>1:
		result.append([clues[-1]+1,upper])
	return result

# Example Usage:

clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99
assert [[2, 2], [4, 49], [51, 74], [76, 99]]==find_missing_clues(clues, lower, upper), "clues = [0, 1, 3, 50, 75] lower = 0 upper = 99--->[2, 2], [4, 49], [51, 74], [76, 99]"
print(find_missing_clues(clues, lower, upper))

clues = [-1]
lower = -1
upper = -1
assert []==find_missing_clues(clues, lower, upper), "clues = [-1] lower = -1 upper = -1--->[]"
print(find_missing_clues(clues, lower, upper))

# Example Output:

# [[2, 2], [4, 49], [51, 74], [76, 99]]
# []
