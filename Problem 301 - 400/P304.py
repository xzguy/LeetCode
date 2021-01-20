class NumMatrix:
    def __init__(self, matrix: [[int]]):
        # convert matrix into cumulative sum
        # matrix[i][j] is the summation of the numbers in
        # rectangle by (0,0) nd (i,j)
        if not matrix:
            return
        row, col = len(matrix), len(matrix[0])
        # first row
        for i in range(1, col):
            matrix[0][i] += matrix[0][i-1]
        # first column
        for i in range(1, row):
            matrix[i][0] += matrix[i-1][0]
        # the rest rectangle
        for i in range(1, row):
            for j in range(1, col):
                matrix[i][j] += matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1]
        self.matrix = matrix
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        matrix = self.matrix
        bigest_rect = matrix[row2][col2]
        if row1 == 0 and col1 == 0:
            return bigest_rect
        elif row1 == 0:
            return bigest_rect - matrix[row2][col1-1]
        elif col1 == 0:
            return bigest_rect - matrix[row1-1][col2]
        else:
            return bigest_rect - matrix[row2][col1-1] - matrix[row1-1][col2] + matrix[row1-1][col1-1]