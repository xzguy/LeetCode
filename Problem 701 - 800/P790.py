class Solution:
    '''
    To solve this problem, we have two steps.
    In the first step, we calculate the number of tiling for
    non-decomposable length of i.
    In the second step, for given N, calculate all possible
    decomposition of integers.
    '''
    def numTilings(self, N: int) -> int:
        if N <= 2:
            return N
        # the number of monatomic tiling for a length
        monatomic = [2] * (N+1)
        monatomic[0] = monatomic[1] = monatomic[2] = 1

        # dictionary for list of all possible decompositions for a length
        # for each number from 1 to N, we need one such dictionary
        int_decomp_list = [{} for _ in range(N+1)]
        # for number 1, the decomposition of size 1 is only [1]
        int_decomp_list[1][1] = [[1]]
        for i in range(2, N+1):
            # the decomposition of size 1 is itself only
            int_decomp_list[i][1] = [[i]]
            # the decomposition of size N is all '1's
            int_decomp_list[i][i] = [[1]*i]
            for j in range(2, i):
                int_decomp_list[i][j] = []
                for k in range(1, i-j+2):
                    for x in int_decomp_list[i-k][j-1]:
                        int_decomp_list[i][j].append([k] + x)  
        
        res = 0
        for j in range(1, N+1):
            for k in range(len(int_decomp_list[N][j])):
                tmp = 1
                for n in int_decomp_list[N][j][k]:
                    tmp *= monatomic[n]
                res += tmp % (10**9+7)
        return res % (10**9+7)

    # dp, much faster method
    # dp[n] = dp[atomic prefix] * dp[n - length of atomic prefix]
    def numTilings_1(self, N: int) -> int:
        if N <= 2:
            return N

        dp = [0] * (N+1)
        dp[0] = 1
        for i in range(1, N+1):
            for j in range(1, i+1):
                if j > 2:
                    dp[i] += 2 * dp[i-j] 
                else:
                    dp[i] += dp[i-j]
        return dp[-1] % (10**9+7)

    '''
    The above method can be further improved mathematically.
    dp[n]   = dp[n-1] + dp[n-2] + 2*(dp[n-3] + ... + d[0])
            = dp[n-1] + dp[n-2] + dp[n-3] + dp[n-3] + 2 * (dp[n-4] + ... + d[0])
            = dp[n-1] + dp[n-3] + (dp[n-2] + dp[n-3] + 2 * (dp[n-4] + ... + d[0]))
            = dp[n-1] + dp[n-3] + dp[n-1]
            = 2 * dp[n-1] + dp[n-3]
    '''
    def numTilings_2(self, N: int) -> int:
        dp = [0] * (N if N > 3 else 3)
        dp[0] = 1
        dp[1] = 2
        dp[2] = 5
        if N <= 3:
            return dp[N-1]

        for i in range(3, N):
            dp[i] = 2 * dp[i-1] + dp[i-3]
        return dp[-1] % (10**9+7)

sol = Solution()
print(sol.numTilings_2(4))