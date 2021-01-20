def minPathSum(grid: [[int]]) -> int:
    if not grid or not grid[0]: return -1

    for i in range(1, len(grid)):
        grid[i][0] += grid[i-1][0]

    for i in range(1, len(grid[0])):
        grid[0][i] += grid[0][i-1]

    for i in range(1, len(grid)):
        for j in range(1, len(grid[i])):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])

    return grid[-1][-1]

input = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

print(minPathSum(input))