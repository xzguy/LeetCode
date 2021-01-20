class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        if not grid:
            return 0
        n, m = len(grid), len(grid[0])
        island_idx = 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    island_idx += 1
                    stack = [(i, j)]
                    while stack:
                        r, c = stack.pop()
                        if 0 <= r < n and 0 <= c < m and grid[r][c] == "1":
                            grid[r][c] = str(island_idx)
                            stack.extend([(r-1, c), (r+1, c), (r, c-1), (r, c+1)])
        return island_idx-1

sol = Solution()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(sol.numIslands(grid))