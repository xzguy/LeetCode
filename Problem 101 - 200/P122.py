class Solution:
    # brute force, recursive
    def maxProfit_1(self, prices: [int]) -> int:

        def sub(start: int) -> int:
            if start == len(prices):
                return 0
            maximum = 0
            for i in range(start, len(prices)):
                max_profit = 0
                for j in range(i+1, len(prices)):
                    if prices[j] > prices[i]:
                        profit = sub(j+1) + prices[j] - prices[i]
                        if profit > max_profit:
                            max_profit = profit
                if max_profit > maximum:
                    maximum = max_profit
            return maximum
        
        return sub(0)
    
    # the key point in this problem is the strategy for maximum profit:
    # buy at valley, sell at peak
    def maxProfit_2(self, prices: [int]) -> int:
        if len(prices) < 2:
            return 0
        valley = peak = prices[0]
        profit = 0
        for p in prices:
            if p < peak:
                profit += (peak - valley)
                valley = p
            peak = p
        if peak == prices[-1]:
            profit += (peak - valley)
        return profit

    # same strategy, another way, maybe more clear
    def maxProfit_3(self, prices: [int]) -> int:
        if len(prices) < 2:
            return 0
        valley = peak = prices[0]
        profit = 0
        i = 0
        while i < len(prices)-1:
            # first find valley
            while i < len(prices)-1 and prices[i] >= prices[i+1]:
                i += 1
            valley = prices[i]
            # then find the peak
            while i < len(prices)-1 and prices[i] <= prices[i+1]:
                i += 1
            peak = prices[i]
            profit += peak - valley
        return profit

    # another strategy:
    # if tomorrow's price is higher than today's, 
    # we buy it today and sell tomorrow. Otherwise, we don't.
    def maxProfit(self, prices: [int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
        return profit

Input = [7,1,5,3,6,4]

Input = [7,6,4,3,1]
Input = [1,2,3,4,5]
sol = Solution()
print(sol.maxProfit(Input))