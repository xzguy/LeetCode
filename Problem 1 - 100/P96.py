class Solution:
    def numTrees(self, n: int) -> int:
        # number of unique BST for 0, 1, 2 nodes
        dp = [1, 1, 2]
        if n <= 2:
            return dp[n]
        # there are total i nodes
        for i in range(3, n+1):
            num = 0
            # j-th node is the root
            for j in range(1, i+1):
                num += dp[j-1] * dp[i-j]
            dp.append(num)
        return dp[-1]


sol = Solution()
print(sol.numTrees(5))