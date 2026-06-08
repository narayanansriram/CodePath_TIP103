def local_maximums(grid):
	R = len(grid)
	C = len(grid[0])
	nR = R-2
	nC = C-2
	newGrid = [[0 for _ in range(nC)] for _ in range(nR)]
	for r in range(1,R-1):
		for c in range(1,C-1):
			centerR=r
			centerC=c
			localMax=0
			# print(centerR-nR//2,centerR+nR//2+1,centerC-nC//2,centerC+nC//2+1)
			for sr in range(centerR-1,centerR+2):
				for sc in range(centerC-1,centerC+2):
					# print(sr,sc,grid[sr][sc])
					localMax=max(localMax,grid[sr][sc])
			newGrid[r-1][c-1]=localMax
			# print("---")
	return newGrid

# Example Usage:

grid = [
	[9, 9, 8, 1],
	[5, 6, 2, 6],
	[8, 2, 6, 4],
	[6, 2, 2, 2]
]
print(local_maximums(grid))

grid = [
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 2, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1]
]
print(local_maximums(grid))

# Example Output:

# [[9, 9], [8, 6]]
# [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
