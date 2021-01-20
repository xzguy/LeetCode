class Solution:
    def maximalSquare(self, matrix: [[str]]) -> int:
        if not matrix:
            return 0
        mat = []
        for i in range(len(matrix)):
            mat.append(list(map(int, matrix[i])))
        # first column and row
        res = max(mat[0])
        for i in range(len(mat)):
            res = max(res, mat[i][0])
        # the rest of rectangle
        for i in range(1, len(mat)):
            for j in range(1, len(mat[0])):
                if mat[i][j] == 1:
                    mat[i][j] = 1 + min(mat[i-1][j-1], mat[i][j-1], mat[i-1][j])
                    res = max(res, mat[i][j])
        return res**2

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
matrix = [["0","1"]]
sol = Solution()
print(sol.maximalSquare(matrix))        