# mathematical method
def uniquePaths(m: int, n: int) -> int:

    def NChooseK(N: int, K: int) -> int:
        if K > N-K:
            return NChooseK(N, N-K)
        i = 0
        res = 1
        while i < K:
            res *= (N-i)
            i += 1
        i = 0
        while i < K:
            res /= (K-i)
            i += 1
        return int(res)

    return NChooseK(m+n-2, n-1)

# dp
def uniquePaths_1(m: int, n: int) -> int:
    dp = [[1] * m for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]


print(uniquePaths_1(3,7))