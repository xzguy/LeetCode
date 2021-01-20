class Solution:
    # top to down
    def minimumTotal(self, triangle: [[int]]) -> int:
        for r in range(1, len(triangle)):
            triangle[r][0] += triangle[r-1][0]
            triangle[r][-1] += triangle[r-1][-1]
            for i in range(1, len(triangle[r])-1):
                triangle[r][i] += min(triangle[r-1][i-1], triangle[r-1][i])
        return min(triangle[-1])

    # bottom to top
    def minimumTotal_1(self, triangle: [[int]]) -> int:
        for r in range(len(triangle)-1, 0, -1):
            for j in range(0, r):
                triangle[r-1][j] += \
                    min(triangle[r][j], triangle[r][j+1])
        return triangle[0][0]

input = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
sol = Solution()
print(sol.minimumTotal(input))