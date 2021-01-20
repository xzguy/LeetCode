class Solution:
    # recursive, slow method exponential time
    def findMaxForm(self, strs: [str], m: int, n: int) -> int:
        zeros_ones = []
        for s in strs:
            zeros = 0
            for c in s:
                if c == "0":
                    zeros += 1
            zeros_ones.append((zeros, len(s)-zeros))

        def sub(zeros_ones_list: [tuple], m: int, n: int) -> int:
            if m == 0 and n == 0:
                return 0
            res = 0
            for z_o in zeros_ones_list:
                if z_o[0] <= m and z_o[1] <= n:
                    zeros_ones_list.remove(z_o)
                    res = max(res, 1 + sub(zeros_ones_list, m-z_o[0], n-z_o[1]))
                    zeros_ones_list.append(z_o)
            return res

        return sub(zeros_ones, m, n)
    
    # dp, space complexity O(m*n)
    def findMaxForm_1(self, strs: [str], m: int, n: int) -> int:
        memo = [[0] * (n+1) for _ in range(m+1)]
        for s in strs:
            num_zeros = 0
            for c in s:
                if c == "0":
                    num_zeros += 1
            num_ones = len(s)-num_zeros
            # memo[i][j] = the max number of strings that can be formed with i 0's and j 1's
            # direction of loops matter
            for i in range(m, num_zeros-1, -1):
                for j in range(n, num_ones-1, -1):
                    memo[i][j] = max(memo[i][j], memo[i-num_zeros][j-num_ones]+1)
        return memo[m][n]

    # dp, knapsack way, easier to understand, space complexity O(m*n*len(strs))
    # dp[i][j][k] means the maximum number of strings we can get from
    # the first i argument strs using limited j number of '0's and k number of '1's.
    # for current str i, there are two decisions, use it or not
    def findMaxForm_2(self, strs: [str], m: int, n: int) -> int:
        dp = [[[0] * (n+1) for _ in range(m+1)] for _ in range(len(strs)+1)]
        for i in range(1, len(strs)+1):
            num_zeros = 0
            for c in strs[i-1]:
                if c == "0":
                    num_zeros += 1
            num_ones = len(strs[i-1]) - num_zeros
            for j in range(m+1):
                for k in range(n+1):
                    if j >= num_zeros and k >= num_ones:
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-num_zeros][k-num_ones]+1)
                    else:
                        dp[i][j][k] = dp[i-1][j][k]
        return dp[-1][-1][-1]

strs = ["10","0001","111001","1","0"]
m = 5
n = 3
sol = Solution()
print(sol.findMaxForm_2(strs, m, n))