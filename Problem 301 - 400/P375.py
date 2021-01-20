class Solution:
    # dp bottom-up
    # dp[i][j] means the minimum pay to surely win the guess for range(i, j+1)
    # dp[i][j] = k + max(dp[i][k-1], dp[k+1][j]), get minimum for k in range(i, j+1)
    def getMoneyAmount(self, n: int) -> int:
        # add dummy space at both ends for easier code
        dp = [[0] * (n+2) for _ in range(n+2)]
        # since all dp[i][i] is zero, we can start from length of 2
        for l in range(2, n+1):
            for i in range(1, n+1-l+1):
                j = i+l-1
                dp[i][j] = float('inf')
                for k in range(i, j+1):
                    dp[i][j] = min(dp[i][j], k + max(dp[i][k-1], dp[k+1][j]))
        return dp[1][n]