class Solution:
    def minFallingPathSum(self, A: [[int]]) -> int:
        if not A:
            return 0
        row, col = len(A), len(A[0])
        for r in range(1, row):
            for c in range(col):
                pre_min = A[r-1][c]
                for d in [-1, 1]:
                    if 0 <= c+d < col:
                        pre_min = min(pre_min, A[r-1][c+d])
                A[r][c] += pre_min
        return min(A[-1])
                    
