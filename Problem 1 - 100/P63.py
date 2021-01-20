# dp
def uniquePathsWithObstacles(obstacleGrid: [[int]]) -> int:
    if not obstacleGrid or not obstacleGrid[0]:
        return 0
    row = len(obstacleGrid)
    col = len(obstacleGrid[0])
    dict = [[0 for _ in range(col)] for _ in range(row)]
    if obstacleGrid[0][0] == 1:
        return 0
    dict[0][0] = 1

    for i in range(1,row):
        if obstacleGrid[i][0] == 1:
            break
        else:
            dict[i][0] = dict[i-1][0]

    for j in range(1,col):
        if obstacleGrid[0][j] == 1:
            break
        else:
            dict[0][j] = dict[0][j-1]

    for i in range(1,row):
        for j in range(1,col):
            if obstacleGrid[i][j] == 1:
                dict[i][j] = 0
            else:
                dict[i][j] = dict[i-1][j] + dict[i][j-1]
    return dict[-1][-1]

# almost same method and same code
def uniquePathsWithObstacles_1(obstacleGrid: [[int]]) -> int:
    if not obstacleGrid:
        return 0
    row, col = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0] * (col+1) for _ in range(row+1)]
    if obstacleGrid[0][0] == 1:
        return 0
    dp[1][1] = 1
    for i in range(1, row+1):
        for j in range(1, col+1):
            if i == 1 and j == 1:
                continue
            if obstacleGrid[i-1][j-1] == 1:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]


input = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
input = [[0,0]]
print(uniquePathsWithObstacles_1(input))