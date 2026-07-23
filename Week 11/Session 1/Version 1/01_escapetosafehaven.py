# You've just learned of a safe haven at the bottom right corner of the city represented by an m x n matrix grid. However, the city is full of zombie-infected zones. Safe travel zones are marked on the grid as 1s and infected zones are marked as 0s. Given your current position as a tuple in the form (row, column), return True if you can reach the safe haven traveling only through safe zones and False otherwise. From any zone (cell) in the grid you may move up, down, left, or right.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.
    
def can_move_safely(position, grid):
    # if grid[position[0]][position[1]] != 1:
    #     return False
    R = len(grid)
    C = len(grid[0])
    visited = {}
    def dfs(r,c):
        if (r,c) in visited:
            return visited[(r,c)]
        if not (0<=r<R and 0<=c<C):
            return False
        if grid[r][c] != 1:
            return False
        if r==(R-1) and c==(C-1) and grid[r][c]==1:
            return True
        visited[(r,c)]=True
        return dfs(r+1,c) or dfs(r-1,c) or dfs(r,c+1) or dfs(r,c-1)
    return dfs(position[0],position[1])
# Example Usage:

grid = [
    [1, 0, 1, 1, 0], # Row 0
    [1, 1, 1, 1, 0], # Row 1
    [0, 0, 1, 1, 0], # Row 2
    [1, 0, 1, 1, 1]  # Row 3
]

position_1 = (0, 0)
position_2 = (0, 4)
position_3 = (3, 0)

print(can_move_safely(position_1, grid))
print(can_move_safely(position_2, grid))
print(can_move_safely(position_3, grid))

# Example Output:

# True
# Example 1 Explanation: Can follow the path (0, 0) -> (1, 0) -> (1, 1) -> (1, 2) -> 
# (2, 2) -> (3, 2) -> (3, 3) -> (3, 4)

# True
# Example 2 Explanation: Although we start in an unsafe position, we can immediately
# arrive in a safe position and from there safely travel to the bottom right corner (3, 4).

# False
