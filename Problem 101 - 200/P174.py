class Solution:
    '''
    The key point in this problem is the direction of
    2D table travesal. Due to the inherent property of
    the game. It is more reasonable and easy to traverse
    from Princess to Valian Knight.
    '''
    def calculateMinimumHP(self, dungeon: [[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float("inf")]* (n+1) for _ in range(m+1)]
        dp[m-1][n], dp[m][n-1] = 1, 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                need = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
                dp[i][j] = max(need, 1)
        return dp[0][0]
        
input = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
input = [[1,-3,3],[0,-2,0],[-3,-3,-3]]
sol = Solution()
print(sol.calculateMinimumHP(input))