class Solution:
    # direct modeling
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if target < d or target > f*d:
            return 0
        if d == 1:
            return 1
        # after first rolling, num[i] is the number of occurrence for i
        num = [1] * (f+1)
        for i in range(2, d+1):
            # for i-th rolling, possible number is in [i, i*f]
            new_num = [0] * (i*f + 1)
            for j in range(i-1, (i-1)*f+1):
                for k in range(1, f+1):
                    new_num[j + k] += num[j]
            num = new_num
        return num[target] % (10**9 + 7)

    # dp, use more space than the above
    def numRollsToTarget_1(self, d: int, f: int, target: int) -> int:
        dp = [[0] * (target+1) for _ in range(d+1)]
        dp[0][0] = 1
        for i in range(1, d+1):
            for j in range(1, target+1):
                k = 1
                while k <= f and k <= j:
                    dp[i][j] += dp[i-1][j-k]
                    k += 1
        return dp[-1][-1] % (10**9 + 7)