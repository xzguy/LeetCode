from functools import lru_cache

class Solution:
    # the input days is in strictly increasing order.
    # recursive method
    def mincostTickets(self, days: [int], costs: [int]) -> int:
        if not days:
            return 0
        # for the first day, there are three decisions
        buy_1day_pass = self.mincostTickets(days[1:], costs) + costs[0]
        buy_7day_pass = self.mincostTickets([x for x in days if x >= days[0] + 7], costs) + costs[1]
        buy_30day_pass = self.mincostTickets([x for x in days if x >= days[0] + 30], costs) + costs[2]
        return min(buy_1day_pass, buy_7day_pass, buy_30day_pass)

    # dp memo, this method can tell the direction of filling the memo
    # this direction is important for bottom-up dp!!
    def mincostTickets_1(self, days: [int], costs: [int]) -> int:

        # one pointer (days list index) for days list slicing
        def sub(start: int, memo: dict) -> int:
            if start == len(days):
                return 0
            if start not in memo:
                # for the day start, there are three decisions
                buy_1day_pass = sub(start+1, memo) + costs[0]
                i = start+1
                while i < len(days) and days[i] < days[start]+7:
                    i += 1
                buy_7day_pass = sub(i, memo) + costs[1]
                while i < len(days) and days[i] < days[start]+30:
                    i += 1
                buy_30day_pass = sub(i, memo) + costs[2]
                memo[start] = min(buy_1day_pass, buy_7day_pass, buy_30day_pass)
            return memo[start]

        if not days:
            return 0
        
        return sub(0, {})

    # dp bottom-up, array building direction inspiration comes from memo method
    # dp[i] means the minimum cost for travel from day i to the end
    # dp[i] = min(dp[i+1]+costs[0], dp[i+7]+costs[1], dp[i+30]+costs[2])
    def mincostTickets_2(self, days: [int], costs: [int]) -> int:
        dayset = set(days)
        # there are at most 366 days a year, plus at most 30 dummy days at the end
        dp = [0] * (366+30)
        for i in range(365, -1, -1):
            if i in dayset:
                dp[i] = min(dp[i+1]+costs[0], dp[i+7]+costs[1], dp[i+30]+costs[2])
            else:
                dp[i] = dp[i+1]
        return dp[0]

    # dp, use python Least Recently Used cache instead of array in above method
    # remove the line: '@lru_cache(None)' will make it equivalent to recursive
    def mincostTickets_3(self, days: [int], costs: [int]) -> int:
        dayset = set(days)
        durations = [1, 7, 30]

        @lru_cache(None)
        def cost_from_i_to_end(i: int) -> int:
            if i > 366:
                return 0
            elif i in dayset:
                return min(cost_from_i_to_end(i + d) + c for c,d in zip(costs, durations))
            else:
                return cost_from_i_to_end(i+1)

        return cost_from_i_to_end(1)

    # similar strategy as the above, thinking of days instead of all 366 possible days
    def mincostTickets_4(self, days: [int], costs: [int]) -> int:
        N = len(days)
        durations = [1 ,7, 30]

        @lru_cache
        def cost_from_days_i_to_end(i: int) -> int:
            if i >= N:
                return 0

            res = float('inf')
            j = i
            # in the following loops, costs and durations are strictly increasing,
            # so j is not necessarily re-initialized.
            for c, d in zip(costs, durations):
                # j is the smallest days index for next function call
                while j < N and days[j] < days[i] + d:
                    j += 1
                res = min(res, cost_from_days_i_to_end(j) + c)
            return res
        
        return cost_from_days_i_to_end(0)