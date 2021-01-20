class Solution:
    # double traverse, O(n^2)
    def maxProfit_1(self, prices: [int]) -> int:
        if len(prices) < 2:
            return 0
        profit = 0
        for sell in range(1, len(prices)):
            for buy in range(sell):
                profit = max(profit, prices[sell] - prices[buy])
        return profit
    
    # maintain one variable minimum buy price,
    # if next price is higher, consider whether it contributes to higher profit
    # else if lower, update the minimum buy price.
    def maxProfit_2(self, prices: [int]) -> int:
        profit = 0
        min_buy_price = None
        for i in range(len(prices)):
            if min_buy_price == None:
                min_buy_price = prices[i]
            elif prices[i] < min_buy_price:
                min_buy_price = prices[i]
            elif prices[i] > min_buy_price:
                profit = max(profit, prices[i]-min_buy_price)
        return profit

    # symmetric solution with maximum sell instead
    def maxProfit(self, prices: [int]) -> int:
        profit = 0
        max_sell_price = None
        for i in range(len(prices)-1, -1, -1):
            if max_sell_price == None:
                max_sell_price = prices[i]
            elif prices[i] > max_sell_price:
                max_sell_price = prices[i]
            elif prices[i] < max_sell_price:
                profit = max(profit, max_sell_price - prices[i])
        return profit

Input = [7,1,5,3,6,4]
Input = [7,6,4,3,1]
Input = [2,1,2,1,0,1,2]
Input = [6,1,3,2,4,7]

sol = Solution()
print(sol.maxProfit(Input))