def diagonal_sum(grid):
	primary = 0
	n = len(grid)
	for i in range(n):
		primary+=grid[i][i]
		j = n-1-i
		# print(i,j)
		if i!=j:
			primary+=grid[i][j]
	return primary
		

# Example Usage

grid = [
	[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(diagonal_sum(grid))

grid = [
	[1, 1, 1, 1],
    [1, 1, 1, 1],
	[1, 1, 1, 1],
    [1, 1, 1, 1]
]
print(diagonal_sum(grid))

grid = [
	[5]
]
print(diagonal_sum(grid))

# Example Output:

# 25
# 8
# 5
