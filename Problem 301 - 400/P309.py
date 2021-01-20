class Solution:
    '''
    dp[i] means the maximum profit from day 1 to day i
    dp[i] = if sell day i, max(prices[i] - prices[j] + dp[j-2], for 1 <= j < i)
    if not sell day i, dp[i-1]
    '''
    def maxProfit(self, prices: [int]) -> int:
        N = len(prices)
        dp = [0] * (N + 1)
        for i in range(2, N + 1):
            # not sell at day i
            dp[i] = dp[i-1]
            # sell at day i, bought at day j
            for j in range(1, i):
                if j == 1:
                    dp[i] = max(dp[i], prices[i-1] - prices[j-1])
                else:
                    dp[i] = max(dp[i], prices[i-1] - prices[j-1] + dp[j-2])
        return dp[-1]

    # an improved version of the above method
    # for j loop, we only want to max: " - prices[j-1] + dp[j-2]"
    # so store this value
    # the following mathod can be further simplified, but logically may not be this easy
    # to calculate dp[i], only dp[i-1] and dp[i-2] are needed, so space complexity can be lower.
    def maxProfit_1(self, prices: [int]) -> int:
        N = len(prices)
        dp = [0] * (N + 1)
        min_buy = float('-inf')
        for i in range(2, N + 1):
            # not sell at day i
            dp[i] = dp[i-1]
            # sell at day i, bought at day j
            j = i-1
            if j == 1:
                min_buy = max(min_buy, -prices[j-1])
            else:
                min_buy = max(min_buy, -prices[j-1] + dp[j-2])
            dp[i] = max(dp[i], prices[i-1] + min_buy)
        return dp[-1]