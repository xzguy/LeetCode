class Solution:
    def setZeroes(self, matrix: [[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        row_set, col_set = set(), set()

        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    row_set.add(r)
                    col_set.add(c)

        for r in range(row):
            for c in range(col):
                if r in row_set or c in col_set:
                    matrix[r][c] = 0