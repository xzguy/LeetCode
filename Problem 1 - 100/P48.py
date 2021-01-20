def rotate(matrix: [[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        half = N//2 + N%2

        for i in range(half):
            for j in range(i, N-i-1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[N-1-j][i]
                matrix[N-1-j][i] = matrix[N-1-i][N-1-j]
                matrix[N-1-i][N-1-j] = matrix[j][N-1-i]
                matrix[j][N-1-i] = temp

matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
rotate(matrix)
print(matrix)
