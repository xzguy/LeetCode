class Solution:
    # direct modeling with memo to improve (still slow)
    def maxCoins(self, nums: [int]) -> int:
        
        def sub(A: [int], memo: dict) -> int:
            if len(A) == 1:
                return A[0]
            if tuple(A) not in memo:
                res = 0
                for i in range(len(A)):
                    if i == 0:
                        left = 1
                    else:
                        left = A[i-1]
                    if i == len(A)-1:
                        right = 1
                    else:
                        right = A[i+1]
                    res = max(res, left*A[i]*right + sub(A[:i] + A[i+1:], memo))
                memo[tuple(A)] = res
            return memo[tuple(A)]
        
        return sub(nums, {})

    '''
    The key point here is the meaning of dp[i][j].
    dp[i][j] is the maximum coins if we burst all balloons in range(i, j+1)
    for every dp[i][j], we should have the last balloons to burst, let's say it is k.
    dp[i][j] = d[i][k-1] + d][k+1][j] + nums[i-1] * nums[k] * nums[j+1]
    The most import part is, since the k is the last balloon to burst, the coins
    for bursting k is nums[i-1] * nums[k] * nums[j+1]
    '''

    # dp bottom-up, similar to the matrix chain product problem
    # in the book 'Introduction to Algorithms'
    def maxCoins_1(self, nums: [int]) -> int:
        N = len(nums)
        # adding ones at the both ends for easier code
        A = [1] + nums + [1]
        dp = [[0] * (N+2) for _ in range(N+2)]
        for l in range(1, N+1):
            for i in range(1, N+1-l+1):
                j = i + l - 1
                for k in range(i, j+1):
                    dp[i][j] = max(dp[i][j], dp[i][k-1] + dp[k+1][j] + A[i-1] * A[k] * A[j+1])
        return dp[1][N]

nums = [3,1,5,8]
sol = Solution()
print(sol.maxCoins_1(nums))