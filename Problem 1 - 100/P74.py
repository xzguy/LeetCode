class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        row = len(matrix)
        col = len(matrix[0])

        l, r = 0, row * col - 1
        while (l != r):
            mid = (l + r - 1) // 2
            if target <= matrix[mid // col][ mid % col]:
                r = mid
            else:
                l = mid + 1
        return target == matrix[l // col][l % col]

sol = Solution()
matrix = [
    [-8, -7],
    [-5, -5]
]
print(sol.searchMatrix(matrix, 0))
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
print(sol.searchMatrix(matrix, 3))
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
print(sol.searchMatrix(matrix, 13))