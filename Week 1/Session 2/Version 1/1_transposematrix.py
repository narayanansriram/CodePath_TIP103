def transpose(matrix):
    R = len(matrix)
    C = len(matrix[0])
    newMatrix = [[0 for _ in range(R)] for _ in range(C)]
    for r in range(R):
        for c in range(C):
            newMatrix[c][r]=matrix[r][c]
    return newMatrix

# Example Usage

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(transpose(matrix))
assert [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
] == transpose(matrix), "[[1, 2, 3], [4, 5, 6], [7, 8, 9]] transposes to [[1, 4, 7], [2, 5, 8], [3, 6, 9]]"

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose(matrix))
assert [
    [1, 4],
    [2, 5],
    [3, 6]
] == transpose(matrix), "[[1, 2, 3],[4, 5, 6]] transposes to [[1, 4], [2, 5], [3, 6]]"


# Example Output:

# [
#     [1, 4, 7],
#     [2, 5, 8],
#     [3, 6, 9]
# ]
# [
#     [1, 4],
#     [2, 5],
#     [3, 6]
# ]
