class Solution:
    # dp, memo, easy to model
    def numWays(self, steps: int, arrLen: int) -> int:
        
        def sub(step: int, pos: int, memo: dict) -> int:
            if step == 0:
                if pos == 0:
                    return 1
                else:
                    return 0
            if (step, pos) not in memo:
                stay = sub(step-1, pos, memo)
                left = 0
                if pos > 0:
                    left = sub(step-1, pos-1, memo)
                right = 0
                if pos < arrLen-1:
                    right = sub(step-1, pos+1, memo)
                memo[step, pos] = stay + left + right
            return memo[step, pos]

        return sub(steps, 0, {}) % (10 ** 9 + 7)

    # dp, bottom-up
    # dp[i][j] means number of ways to reach index j with i steps
    # dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]
    def numWays_1(self, steps: int, arrLen: int) -> int:
        max_pos = min(steps, arrLen)
        dp = [[0] * max_pos for _ in range(steps+1)]
        dp[0][0] = 1
        for i in range(1, steps+1):
            for j in range(max_pos):
                dp[i][j] = dp[i-1][j]
                if j-1 >= 0:
                    dp[i][j] += dp[i-1][j-1]
                if j+1 < max_pos:
                    dp[i][j] += dp[i-1][j+1]

        return dp[-1][0] % (10 ** 9 + 7)

    def numWays_2(self, steps: int, arrLen: int) -> int:
        mod=10 ** 9 + 7
        # the first zero is dummy for easier summation
        A = [0, 1]
        for t in range(steps):
            A[1:] = [sum(A[i-1:i+2])%mod for i in range(1, min(arrLen+1, steps-t+1, t+3))]
        return A[1] % mod

sol = Solution()
print(sol.numWays_2(3, 2))