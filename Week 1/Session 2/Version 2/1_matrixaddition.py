def add_matrices(matrix1, matrix2):
    R = len(matrix1)
    C = len(matrix1)
    result = [[0 for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            result[r][c]+=(matrix1[r][c]+matrix2[r][c])
    return result           

# Example Usage

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print(add_matrices(matrix1, matrix2))

# Example Output:

[
    [10, 10, 10],
    [10, 10, 10],
    [10, 10, 10]
]
