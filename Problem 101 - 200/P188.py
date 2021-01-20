class Solution:
    def maxProfit(self, k: int, prices: [int]) -> int:
        if len(prices) < 2 or k < 1:
            return 0
        # possible maximum number of transactions
        if 2*k > len(prices):
            k = len(prices) // 2
        dp = [[0]*len(prices) for _ in range(k)]
        # one transaction
        min_buy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] <= min_buy:
                min_buy = prices[i]
            else:
                dp[0][i] = prices[i] - min_buy
        max_profit = max(dp[0])
        # from second to k transactions
        for t in range(1, k):
            max_pre = max(dp[t-1][:2*t])
            min_buy = prices[2*t] - max_pre
            for i in range(2*t+1, len(prices)):
                if dp[t-1][i-1] > max_pre:
                    max_pre = dp[t-1][i-1]
                if prices[i] - max_pre <= min_buy:
                    min_buy = prices[i] - max_pre
                else:
                    dp[t][i] = prices[i] - min_buy
            max_profit = max(max_profit, max(dp[t]))
        return max_profit

sol = Solution()
k = 2
prices = [3,2,6,5,0,3]
k = 2
prices = [2,4,1]
k = 4
prices = [1,2,4,2,5,7,2,4,9,0]
print(sol.maxProfit(k, prices))