class Solution:
    '''
    To build the binary tree, it is equivalent to parenthesize the numbers.
    When adding a pair of parenthesis, the cost is the product of
    maximum of left expression and right expression.
    Similar to the matrix chain product problem, use range.
    dp[i][j] is the minimum cost of binary tree built from arr[i:j]
    dp[i][j] = min([dp[i][k] + dp[k][j] + max(arr[i:k]) * max(arr[k:j]) for k in range(i+1,j)])
    '''
    def mctFromLeafValues(self, arr: [int]) -> int:
        if not arr:
            return 0

        N = len(arr)
        # i at most can be N-2, j at most can be N, k at most N-1
        dp = [[0] * (N+1) for _ in range(N)]
        subtree_max = [[0] * (N+1) for _ in range(N+1)]
        for l in range(2, N+1):
            for i in range(N-l+1):
                j = i + l
                dp[i][j] = float('inf')
                for k in range(i+1, j):
                    subtree_max[i][k] = max(arr[i], subtree_max[i+1][k])
                    subtree_max[k][j] = max(arr[k], subtree_max[k+1][j])
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + subtree_max[i][k] * subtree_max[k][j])
        return dp[0][N]

    '''
    because this cost: max(arr[i:k]) * max(arr[k:j])
    an more efficient greedy method is possible.
    '''
arr = [6,2,4]
sol = Solution()
print(sol.mctFromLeafValues(arr))