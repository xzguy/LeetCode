# Standard library imports
import random

# Local application imports
import sys
sys.path.append('c:\\Users\\ShenChen\\Desktop\\Python_projects\\LeetCode')
import function_exec_time_compare as fetc

class Solution:
    def maxProfit_0(self, prices: [int]) -> int:
        # auxiliary function for one transaction
        def maxProfit_one(start: int, end: int) -> int:
            profit = 0
            min_buy_price = prices[start]
            for i in range(start, end):
                if prices[i] > min_buy_price:
                    profit = max(profit, prices[i] - min_buy_price)
                else:
                    min_buy_price = prices[i]
            return profit

        max_profit = 0
        for p in range(len(prices)):
            cur_profit = maxProfit_one(0, p) + maxProfit_one(p, len(prices))
            max_profit = max(max_profit, cur_profit)
        return max_profit

    # dynamic programming
    # the recursive formula is
    # dp[k, i] = max(dp[k, i-1], prices[i] - prices[j] + dp[k-1, j-1]), j=[0...i-1]
    # it means, for k-th transaction, i-th day price, 
    # if trade, profit is "prices[i] - prices[j] + dp[k-1][j-1], j=[0...i-1]"
    # if not trade, profit is dp[k, i-1], so get their maximum.
    def maxProfit_1(self, prices: [int]) -> int:
        if not prices:
            return 0
        # 3 rows for 0, 1, 2 transations, initialize to zero
        mat = [[0] * len(prices) for _ in range(3)]
        for k in range(1, 3):
            for i in range(1, len(prices)):
                minimum = prices[0]
                for j in range(1, i+1):
                    minimum = min(minimum, prices[j] - mat[k-1][j-1])
                mat[k][i] = max(mat[k][i-1], prices[i]-minimum)
        return mat[-1][-1]
        
    # in the above solution, minimum is repeatedly calculated.
    def maxProfit_2(self, prices: [int]) -> int:
        if not prices:
            return 0
        # 3 rows for 0, 1, 2 transations, initialize to zero
        mat = [[0] * len(prices) for _ in range(3)]
        for k in range(1, 3):
            minimum = prices[0]
            for i in range(1, len(prices)):
                minimum = min(minimum, prices[i] - mat[k-1][i-1])
                mat[k][i] = max(mat[k][i-1], prices[i]-minimum)
        return mat[-1][-1]

    # reduce space from 2-dimensional to 1-dimensional
    def maxProfit_3(self, prices: [int]) -> int:
        if not prices:
            return 0
        dp = [0] * 3
        minimum = [prices[0]] * 3
        for i in range(1, len(prices)):
            for k in range(1,3):
                minimum[k] = min(minimum[k], prices[i] - dp[k-1])
                dp[k] = max(dp[k], prices[i] - minimum[k])
        return dp[2]

    # extend k iteration
    def maxProfit_4(self, prices: [int]) -> int:
        if not prices:
            return 0
        buy1 = buy2 = float('inf')
        profit1 = profit2 = 0
        for i in range(len(prices)):
            buy1 = min(buy1, prices[i])
            profit1 = max(profit1, prices[i] - buy1)
            buy2 = min(buy2, prices[i] - profit1)
            profit2 = max(profit2, prices[i] - buy2)
        return profit2

prices = [3,3,5,0,0,3,1,4]
prices = [1,2,3,4,5]
prices = [7,6,4,3,1]

sol = Solution()

# compare functions execution time
prices = [random.randrange(50) for _ in range(100)]
input_func = random.shuffle
rep = 100
func_list = [sol.maxProfit_0, sol.maxProfit_1, sol.maxProfit_2, sol.maxProfit_3, sol.maxProfit_4]
func_name_list = ["recursive", "Dp1", "Dp2", "Dp3", "Dp4"]
fetc.compare_function_exec_time(prices, input_func, rep, func_list, func_name_list)