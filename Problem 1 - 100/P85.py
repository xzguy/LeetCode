class Solution:
    def maximalRectangle_bf(self, matrix: [[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        max_rect = 0
        for bottom in range(len(matrix)):
            for right in range(len(matrix[bottom])):
                for top in range(bottom+1):
                    for left in range(right+1):
                        rect = True
                        for i in range(top, bottom+1):
                            if not rect:
                                break
                            for j in range(left, right+1):
                                if matrix[i][j] == "0":
                                    rect = False
                                    break
                        if rect:
                            max_rect = max(max_rect, (bottom-top+1)*(right-left+1))
        return max_rect

    def maximalRectangle(self, matrix: [[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        max_rect = 0
        row = len(matrix)
        col = len(matrix[0])
        left, right, height = [0] * col, [col] * col, [0] * col
        for r in range(row):
            cur_left = 0
            cur_right = col
            # height
            for c in range(col):
                if matrix[r][c] == "1": height[c] += 1
                else: height[c] = 0
            # left
            for c in range(col):
                if matrix[r][c] == "1": left[c] = max(left[c], cur_left)
                else: 
                    left[c] = 0
                    cur_left = c+1
            # right
            for c in range(col-1, -1, -1):
                if matrix[r][c] == "1": right[c] = min(right[c], cur_right)
                else:
                    right[c] = col
                    cur_right = c
            # area
            for c in range(col):
                max_rect = max(max_rect, height[c]*(right[c] - left[c]))
        return max_rect

    def maximalRectangle_short(self, matrix: [[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        max_rect = 0
        row = len(matrix)
        col = len(matrix[0])
        left, right, height = [0] * col, [col] * col, [0] * col
        for r in range(row):
            cur_left = 0
            cur_right = col
            # height, left, right
            for c in range(col):
                if matrix[r][c] == "1":
                    height[c] += 1
                    left[c] = max(left[c], cur_left)
                else: 
                    height[c] = 0
                    left[c] = 0
                    cur_left = c+1
                if matrix[r][col - 1 - c] == "1":
                    right[col - 1 - c] = min(right[col - 1 - c], cur_right)
                else:
                    right[col - 1 - c] = col
                    cur_right = col - 1 - c
            # area
            for c in range(col):
                max_rect = max(max_rect, height[c]*(right[c] - left[c]))
        return max_rect

input = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

sol = Solution()
print("brute force:", sol.maximalRectangle_bf(input))
print(sol.maximalRectangle(input))
print("short ver:", sol.maximalRectangle_short(input))