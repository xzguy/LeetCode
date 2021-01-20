class Solution:
    # recursive, dfs
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        # if outside grid, count one
        if not (0 <= i < m and 0 <= j < n):
            return 1
        if N == 0:
            return 0
        path = 0
        for x, y in [[-1,0], [1,0], [0,-1], [0,1]]:
            path += self.findPaths(m, n, N-1, i+x, j+y)
        return path % (10**9+7)

    # dp memo
    def findPaths_1(self, m: int, n: int, N: int, i: int, j: int) -> int:

        def sub(N: int, i: int, j: int, memo: dict) -> int:
            if not (0 <= i < m and 0 <= j < n):
                return 1
            if N == 0:
                return 0
            if (N, i, j) not in memo:
                path = 0
                for x, y in [[-1,0], [1,0], [0,-1], [0,1]]:
                    path += self.findPaths(m, n, N-1, i+x, j+y) % (10**9+7)
                memo[N, i, j] = path
            return memo[N, i, j]

        return sub(N, i, j, {})

    # dp bottom-up
    def findPaths_2(self, m: int, n: int, N: int, i: int, j: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[i][j] = 1
        cnt = 0
        for _ in range(N):
            tmp = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if i == 0:
                        cnt += dp[i][j]
                    if i == m-1:
                        cnt += dp[i][j]
                    if j == 0:
                        cnt += dp[i][j]
                    if j == n-1:
                        cnt += dp[i][j]
                    if i-1 >= 0:
                        tmp[i][j] += dp[i-1][j] % (10**9+7)
                    if i+1 < m:
                        tmp[i][j] += dp[i+1][j] % (10**9+7)
                    if j-1 >= 0:
                        tmp[i][j] += dp[i][j-1] % (10**9+7)
                    if j+1 < n:
                        tmp[i][j] += dp[i][j+1] % (10**9+7)
            dp = tmp
        return cnt % (10**9+7)

m = 1
n = 3
N = 3
i = 0
j = 1
sol = Solution()
print(sol.findPaths_2(m, n, N, i, j))