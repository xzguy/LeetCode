class Solution:
    # recursive method with memo
    def minScoreTriangulation(self, A: [int]) -> int:
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                memo[i, j] = min([dp(i,k) + dp(k,j) + A[i]*A[j]*A[k] for k in range(i+1,j)] or [0])
            return memo[i, j]
            
        return dp(0, len(A)-1)

    # bottom up dynamic programming
    def minScoreTriangulation_1(self, A: [int]) -> int:
        n = len(A)
        dp = [[0] * n for _ in range(n)]
        # distance between i and j is at least 2
        for d in range(2, n):
            for i in range(n-d):
                j = i + d
                dp[i][j] = min(dp[i][k] + dp[k][j] + A[i]*A[j]*A[k] for k in range(i+1, j))
        return dp[0][n-1]