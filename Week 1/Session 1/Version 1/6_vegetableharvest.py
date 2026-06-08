def harvest(vegetable_patch):
	R = len(vegetable_patch)
	C = len(vegetable_patch[0])
	carrots = 0
	for r in range(R):
		for c in range(C):
			if vegetable_patch[r][c]=='c':
				carrots+=1
	return carrots

# Example Usage:

vegetable_patch = [
	['x', 'c', 'x'],
	['x', 'x', 'x'],
	['x', 'c', 'c'],
	['c', 'c', 'c']
]
print(harvest(vegetable_patch))

# Example Output:

# 6
